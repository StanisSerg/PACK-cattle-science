#!/usr/bin/env python3
"""b05-bot.py — Telegram-бот контура сбора данных визитов (WP-117 Ф2, ветвь B-05).

Сценарий (PAD, структура S3):
  /start → кнопки хозяйств → выбор → бот выдаёт ссылку на Google-таблицу хозяйства.
  Фото → папка «фото» хозяйства на Drive.
  Голосовое → транскрибация (Yandex SpeechKit) → аудио в «аудио», текст в «транскрипты»
  + ответ ботом с текстом (помощник видит, что записалось).
  /done — завершить визит (сброс выбора хозяйства).

Конфиг через переменные окружения:
  B05_BOT_TOKEN   — токен Telegram-бота (от @BotFather)
  B05_OAUTH_TOKEN — путь к OAuth-токену пилота (default: /home/asus/IWE/.secrets/b05-oauth-token.json)
  YC_API_KEY      — API-ключ Yandex Cloud (SpeechKit)
  YC_FOLDER_ID    — folderId Yandex Cloud (обязателен для SpeechKit)

Запуск: PYTHONPATH=/home/asus/IWE/.tmp-tools/b05-google-libs python3 b05-bot.py

Ограничение SpeechKit sync API: аудио ≤1 МБ (~1 минута). Длинные голосовые —
пометка «слишком длинное», аудио всё равно сохраняется (транскрибация позже).
"""
import asyncio
import datetime
import json
import logging
import os
import tempfile
import time
import urllib.request
from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (ApplicationBuilder, CallbackQueryHandler,
                          CommandHandler, ContextTypes, MessageHandler, filters)

BASE = Path(__file__).resolve().parent.parent
MANIFEST_PATH = BASE / "google-infra-manifest.json"
OAUTH_TOKEN = Path(os.environ.get("B05_OAUTH_TOKEN", "/home/asus/IWE/.secrets/b05-oauth-token.json"))
BOT_TOKEN = os.environ.get("B05_BOT_TOKEN", "")


def _secret(env_name: str, filename: str) -> str:
    """Ключ из переменной окружения или из файла .secrets (по умолчанию)."""
    v = os.environ.get(env_name, "")
    if v:
        return v
    p = Path(f"/home/asus/IWE/.secrets/{filename}")
    return p.read_text().strip() if p.exists() else ""


YC_API_KEY = _secret("YC_API_KEY", "yc-api-key.txt")
YC_FOLDER_ID = _secret("YC_FOLDER_ID", "yc-folder-id.txt")
YC_S3_KEY_ID = _secret("YC_S3_KEY_ID", "yc-s3-key-id.txt")
YC_S3_SECRET = _secret("YC_S3_SECRET", "yc-s3-secret.txt")
YC_BUCKET = os.environ.get("YC_BUCKET", "b05-audio-1")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("b05-bot")

SCOPES = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]


def load_manifest() -> dict:
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


def drive_service():
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    with open(OAUTH_TOKEN) as f:
        t = json.load(f)
    creds = Credentials(
        token=t.get("access_token"), refresh_token=t["refresh_token"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=t["client_id"], client_secret=t["client_secret"], scopes=SCOPES)
    return build("drive", "v3", credentials=creds)


def upload_to_drive(drive, local_path: str, name: str, folder_id: str) -> str:
    from googleapiclient.http import MediaFileUpload
    media = MediaFileUpload(local_path)
    f = drive.files().create(
        body={"name": name, "parents": [folder_id]},
        media_body=media, fields="id").execute()
    log.info("uploaded %s → %s (%s)", name, folder_id, f["id"])
    return f["id"]


def transcribe_yc_async(audio_path: str, name: str, audio_encoding: str = "OGG_OPUS") -> str | None:
    """Yandex SpeechKit async API: загрузка в Object Storage → longRunningRecognize → текст.

    Работает с аудио любой разумной длины (в отличие от sync API, ≤1 МБ).
    None — если ключи не настроены.
    """
    if not (YC_API_KEY and YC_FOLDER_ID and YC_S3_KEY_ID and YC_S3_SECRET):
        return None
    # SpeechKit не принимает m4a/aac напрямую — конвертируем в ogg/opus (ffmpeg-static)
    converted = None
    if audio_encoding != "OGG_OPUS":
        import subprocess
        import imageio_ffmpeg
        converted = tempfile.NamedTemporaryFile(suffix=".ogg", delete=False).name
        ff = imageio_ffmpeg.get_ffmpeg_exe()
        r = subprocess.run([ff, "-y", "-i", audio_path, "-c:a", "libopus", converted],
                           capture_output=True)
        if r.returncode != 0:
            log.error("ffmpeg конвертация %s упала: %s", audio_path, r.stderr.decode()[:300])
            return None
        audio_path = converted
        audio_encoding = "OGG_OPUS"
    import boto3
    s3 = boto3.client("s3", endpoint_url="https://storage.yandexcloud.net",
                      aws_access_key_id=YC_S3_KEY_ID, aws_secret_access_key=YC_S3_SECRET)
    ext = Path(audio_path).suffix  # после возможной конвертации — .ogg
    obj_key = f"voice/{name}{ext}"
    with open(audio_path, "rb") as f:
        s3.put_object(Bucket=YC_BUCKET, Key=obj_key, Body=f.read())
    if converted and os.path.exists(converted):
        os.unlink(converted)  # конверт нужен был только для загрузки в бакет

    def _req(url, body=None):
        data = json.dumps(body).encode() if body else None
        req = urllib.request.Request(url, data=data, headers={
            "Authorization": f"Api-Key {YC_API_KEY}", "Content-Type": "application/json"})
        return json.load(urllib.request.urlopen(req, timeout=60))

    op = _req("https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize", {
        "config": {"specification": {"languageCode": "ru-RU", "model": "general",
                                     "audioEncoding": audio_encoding}},
        "folderId": YC_FOLDER_ID,
        "audio": {"uri": f"https://storage.yandexcloud.net/{YC_BUCKET}/{obj_key}"},
    })
    op_id = op["id"]
    log.info("stt operation %s для %s", op_id, name)
    text = None
    for _ in range(240):  # до ~20 минут ожидания (5с × 240)
        time.sleep(5)
        st = _req(f"https://operation.api.cloud.yandex.net/operations/{op_id}")
        if st.get("done"):
            if "error" in st:
                log.error("stt ошибка: %s", st["error"])
            else:
                chunks = st.get("response", {}).get("chunks", [])
                text = " ".join(c["alternatives"][0]["text"]
                                for c in chunks if c.get("alternatives"))
            break
    # прибраться в бакете — аудио уже на Drive
    try:
        s3.delete_object(Bucket=YC_BUCKET, Key=obj_key)
    except Exception as e:
        log.warning("не удалось удалить %s из бакета: %s", obj_key, e)
    return text


def farm_keyboard(manifest: dict) -> InlineKeyboardMarkup:
    buttons = [[InlineKeyboardButton(f["name"], callback_data=f"farm:{f['slug']}")]
               for f in manifest["farms"]]
    return InlineKeyboardMarkup(buttons)


def farm_by_slug(manifest: dict, slug: str) -> dict | None:
    return next((f for f in manifest["farms"] if f["slug"] == slug), None)


async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    manifest = load_manifest()
    await update.message.reply_text(
        "Визит в хозяйство. Выберите хозяйство:",
        reply_markup=farm_keyboard(manifest))


async def on_farm_choice(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    slug = query.data.split(":", 1)[1]
    manifest = load_manifest()
    farm = farm_by_slug(manifest, slug)
    ctx.user_data["farm"] = slug
    sheet_url = f"https://docs.google.com/spreadsheets/d/{farm['spreadsheet_id']}"
    await query.message.reply_text(
        f"Хозяйство: {farm['name']}\n\n"
        f"1. Таблица для замеров: {sheet_url}\n"
        f"2. Фото (доение из компьютера, журнал, навоз, упитанность) — отправляйте сюда.\n"
        f"3. Голосовое с комментариями — сюда же.\n\n"
        f"Когда закончите — /done")


async def on_photo(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    slug = ctx.user_data.get("farm")
    if not slug:
        await update.message.reply_text("Сначала выберите хозяйство: /start")
        return
    manifest = load_manifest()
    farm = farm_by_slug(manifest, slug)
    photo = update.message.photo[-1]  # максимальное разрешение
    tg_file = await photo.get_file()
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    user = update.message.from_user.username or str(update.message.from_user.id)
    caption = (update.message.caption or "").strip()
    suffix = f"_{caption[:40]}" if caption else ""
    name = f"{ts}_{user}{suffix}.jpg"
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        await tg_file.download_to_drive(tmp.name)
        fid = upload_to_drive(drive_service(), tmp.name, name, farm["subfolders"]["фото"])
    os.unlink(tmp.name)
    await update.message.reply_text(f"Фото сохранено ({farm['name']}/фото): {name}")


async def on_voice(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    slug = ctx.user_data.get("farm")
    if not slug:
        await update.message.reply_text("Сначала выберите хозяйство: /start")
        return
    manifest = load_manifest()
    farm = farm_by_slug(manifest, slug)
    tg_file = await update.message.voice.get_file()
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    user = update.message.from_user.username or str(update.message.from_user.id)
    name = f"{ts}_{user}"
    tmp = tempfile.NamedTemporaryFile(suffix=".oga", delete=False)
    tmp.close()
    await tg_file.download_to_drive(tmp.name)
    drive = drive_service()
    upload_to_drive(drive, tmp.name, f"{name}.oga", farm["subfolders"]["аудио"])
    await update.message.reply_text(
        f"Принято ({farm['name']}): аудио на Диске, расшифровка появится в папке «транскрипты».")
    # транскрибация — в фоне, результат сразу на Drive (не в чат), по уточнению пилота 05.09
    asyncio.create_task(_transcribe_and_upload(tmp.name, name, farm["subfolders"]["транскрипты"]))


async def _transcribe_and_upload(audio_path: str, name: str, transcripts_folder: str, audio_encoding: str = "OGG_OPUS"):
    try:
        text = await asyncio.to_thread(transcribe_yc_async, audio_path, name, audio_encoding)
        if text:
            with tempfile.NamedTemporaryFile(suffix=".txt", delete=False, mode="w", encoding="utf-8") as tf:
                tf.write(text)
                tf.flush()  # без flush загрузка на Drive читает пустой файл
                upload_to_drive(drive_service(), tf.name, f"{name}.txt", transcripts_folder)
            os.unlink(tf.name)
            log.info("транскрипт %s сохранён на Drive", name)
        else:
            log.warning("транскрибация %s не настроена (нет ключей YC) — только аудио", name)
    except Exception as e:
        log.error("транскрибация %s упала: %s", name, e)
    finally:
        if os.path.exists(audio_path):
            os.unlink(audio_path)


async def cmd_done(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    slug = ctx.user_data.pop("farm", None)
    if slug:
        await update.message.reply_text(
            "Визит завершён. Не забудьте строку в «Журнале визитов» таблицы хозяйства. "
            "Следующий визит — /start")
    else:
        await update.message.reply_text("Визит не был начат. /start")


async def on_audio_file(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """Аудиофайл с телефона (диктофон: m4a/mp3/ogg через «Скрепка → Файл»)."""
    slug = ctx.user_data.get("farm")
    if not slug:
        await update.message.reply_text("Сначала выберите хозяйство: /start")
        return
    manifest = load_manifest()
    farm = farm_by_slug(manifest, slug)
    doc = update.message.audio or update.message.document
    tg_file = await doc.get_file()
    ext = Path(doc.file_name or "audio.m4a").suffix or ".m4a"
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    user = update.message.from_user.username or str(update.message.from_user.id)
    name = f"{ts}_{user}"
    tmp = tempfile.NamedTemporaryFile(suffix=ext, delete=False)
    tmp.close()
    await tg_file.download_to_drive(tmp.name)
    drive = drive_service()
    upload_to_drive(drive, tmp.name, f"{name}{ext}", farm["subfolders"]["аудио"])
    await update.message.reply_text(
        f"Принято ({farm['name']}): запись на Диске, расшифровка появится в папке «транскрипты».")
    # SpeechKit принимает ogg/mp3/wav; m4a может быть отвергнут — тогда только аудио
    encoding = {".mp3": "MP3", ".wav": "LINEAR16", ".m4a": "AAC", ".aac": "AAC"}.get(ext, "OGG_OPUS")
    asyncio.create_task(_transcribe_and_upload(tmp.name, name, farm["subfolders"]["транскрипты"], encoding))


def main():
    if not BOT_TOKEN:
        raise SystemExit("Задайте B05_BOT_TOKEN (токен от @BotFather)")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("done", cmd_done))
    app.add_handler(CallbackQueryHandler(on_farm_choice, pattern=r"^farm:"))
    app.add_handler(MessageHandler(filters.PHOTO, on_photo))
    app.add_handler(MessageHandler(filters.VOICE, on_voice))
    app.add_handler(MessageHandler(filters.AUDIO | filters.Document.AUDIO, on_audio_file))
    log.info("Бот запущен (polling)")
    app.run_polling()


if __name__ == "__main__":
    main()
