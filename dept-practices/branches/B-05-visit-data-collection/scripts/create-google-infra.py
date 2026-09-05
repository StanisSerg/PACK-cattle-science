#!/usr/bin/env python3
"""create-google-infra.py — WP-117 Ф1: создание Google-инфраструктуры контура B-05.

Создаёт по JSON-ключу сервисного аккаунта:
1. 4 Google Sheets (по одному на хозяйство) со вкладками = комплект таблиц B-01
   (состав — DS-cattle-cases/cases/CASE-003…006/raw/README.md).
2. Папки Drive: B-05-visits/<хозяйство>/{фото,аудио,транскрипты}.
3. Шарит таблицы и папки на email пилота (writer).
4. Пишет манифест google-infra-manifest.json (ID таблиц/папок) — бот читает его.

Использование:
  python3 create-google-infra.py --key /path/to/service-account.json --email pilot@gmail.com [--dry-run]

Зависимости: google-api-python-client, google-auth (ставятся в venv, см. README ветви).
"""
import argparse
import json
import sys
from pathlib import Path

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

def make_services(token_path: str):
    """Сервисы от имени пилота (OAuth user credentials с refresh token).

    Сервисный аккаунт не подходит: у него storage quota = 0 — файлы
    (таблицы, фото) он хранить не может. См. разбор в карточке проблемы
    problems/2026-09-05-telegram-bot-sbor-dannyh.md.
    """
    try:
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
    except ImportError:
        sys.exit("Нет зависимостей. Установите: pip install google-api-python-client google-auth")
    with open(token_path) as f:
        t = json.load(f)
    creds = Credentials(
        token=t.get("access_token"),
        refresh_token=t["refresh_token"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=t["client_id"],
        client_secret=t["client_secret"],
        scopes=SCOPES,
    )
    return build("sheets", "v4", credentials=creds), build("drive", "v3", credentials=creds)

# Хозяйства пилота метода (кейсы CASE-003…006, DS-cattle-cases)
FARMS = [
    {"slug": "druzhba-narodov", "name": "Дружба Народов", "case": "CASE-003"},
    {"slug": "belovezhsky", "name": "Беловежский", "case": "CASE-004"},
    {"slug": "sheni-agroprodukt", "name": "Шени-Агропродукт", "case": "CASE-005"},
    {"slug": "tyshkovichi", "name": "Тышковичи", "case": "CASE-006"},
]

# Вкладки = комплект таблиц B-01 (образец форматов — CASE-002).
# В md-таблицах дата — в имени файла; в Sheets дата — первая колонка.
TABS = [
    {"key": "visit_log", "title": "Журнал визитов", "headers": [
        "Дата", "Технолог", "СВ", "Сита", "Жвачка", "Молоко", "Реализация",
        "Переменный набор (что выполнено)", "Неполный замер", "Примечания"]},
    {"key": "milk_dynamics", "title": "Динамика молока", "headers": [
        "Дата", "Дойных голов, гол.", "Реализация, кг", "Удой на дойную корову, л",
        "Жир, %", "Температура днём, °C", "Температура ночью, °C", "Примечания"]},
    {"key": "group_productivity", "title": "Продуктивность групп", "headers": [
        "Дата замера", "Группа", "Голов, гол.", "DIM", "Дни стельности",
        "Продуктивность, л/сут", "Примечание"]},
    {"key": "psps_tmr", "title": "Сита TMR", "headers": [
        "Дата", "Группа", "СВ, %", "Точка отбора", "Проба №",
        "Сито 1 (>19 мм), г", "Сито 1, %", "Сито 2 (8 мм), г", "Сито 2, %",
        "Сито 3 (4.0 мм), г", "Сито 3, %", "Поддон (<1.18 мм), г", "Поддон, %",
        "Всего, г", "Примечания"]},
    {"key": "psps_feeds", "title": "Сита кормов", "headers": [
        "Дата", "Вид корма", "СВ, %", "№ траншеи",
        "Сито 1, г", "Сито 1, %", "Сито 2, г", "Сито 2, %",
        "Сито 3, г", "Сито 3, %", "Поддон, г", "Поддон, %",
        "Всего, г", "pef", "Примечания"]},
    {"key": "zhvachka", "title": "Жвачка", "headers": [
        "Дата", "Группа", "Время относительно кормления, ч", "Голов в группе",
        "Жующих, гол.", "Жующих, %", "Примечания"]},
    {"key": "navoznye_sita", "title": "Навозные сита", "headers": [
        "Дата", "Группа", "ID коровы / проба №", "Верхнее сито, %",
        "Среднее сито, %", "Поддон, %", "Примечания (зерно, частицы, слизь)"]},
    {"key": "ph_mochi", "title": "pH мочи", "headers": [
        "Дата", "ID коровы", "pH", "Время после корма, ч", "Примечания"]},
    {"key": "bcs", "title": "BCS упитанность", "headers": [
        "Дата", "Группа", "ID коровы", "BCS", "Примечания"]},
    {"key": "comfort_air_routine", "title": "Комфорт-воздух-распорядок", "headers": [
        "Дата", "Раздел (стойла/воздух/распорядок)", "Параметр", "Значение", "Примечания"]},
]

DRIVE_SUBFOLDERS = ["фото", "аудио", "транскрипты"]
ROOT_FOLDER_NAME = "B-05-visits"
MANIFEST_PATH = Path(__file__).resolve().parent.parent / "google-infra-manifest.json"


def share(drive, file_id: str, email: str, dry_run: bool):
    if dry_run:
        print(f"  [dry-run] share {file_id} → {email}")
        return
    drive.permissions().create(
        fileId=file_id,
        body={"type": "user", "role": "writer", "emailAddress": email},
        sendNotificationEmail=False,  # иначе срабатывает sharing quota (квота считается по уведомлениям)
        fields="id",
    ).execute()


def find_sheet(drive, title: str, parent: str):
    q = (f"name='{title}' and mimeType='application/vnd.google-apps.spreadsheet' "
         f"and '{parent}' in parents and trashed=false")
    res = drive.files().list(q=q, fields="files(id,name)").execute()
    files = res.get("files", [])
    return files[0]["id"] if files else None


def create_sheet(sheets, drive, farm: dict, parent_folder: str, dry_run: bool) -> str:
    title = f"B-01 замеры — {farm['name']} ({farm['case']})"
    if dry_run:
        print(f"  [dry-run] spreadsheet «{title}», вкладок: {len(TABS)}")
        return f"dry-run-{farm['slug']}"
    existing = find_sheet(drive, title, parent_folder)
    if existing:
        print(f"  ◐ spreadsheet «{title}» уже есть: {existing}")
        return existing
    # создаём через Drive API внутри папки пилота — файл занимает квоту пилота,
    # а не сервисного аккаунта (у СА storage quota = 0, spreadsheets().create → 403)
    f = drive.files().create(body={
        "name": title,
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "parents": [parent_folder],
    }, fields="id").execute()
    sid = f["id"]
    # у новой таблицы есть вкладка по умолчанию — переименуем в первую, добавим остальные
    requests = [
        {"updateSheetProperties": {
            "properties": {"sheetId": 0, "title": TABS[0]["title"]}, "fields": "title"}}
    ] + [
        {"addSheet": {"properties": {"title": t["title"]}}} for t in TABS[1:]
    ]
    sheets.spreadsheets().batchUpdate(
        spreadsheetId=sid, body={"requests": requests}).execute()
    # заголовки столбцов на каждой вкладке
    data = [{
        "range": f"'{t['title']}'!A1",
        "values": [t["headers"]],
    } for t in TABS]
    sheets.spreadsheets().values().batchUpdate(
        spreadsheetId=sid, body={"valueInputOption": "RAW", "data": data}).execute()
    print(f"  ✅ spreadsheet «{title}»: {sid}")
    return sid


def find_folder(drive, name: str, parent: str | None):
    q = f"name='{name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    if parent:
        q += f" and '{parent}' in parents"
    res = drive.files().list(q=q, fields="files(id,name)").execute()
    files = res.get("files", [])
    return files[0]["id"] if files else None


def create_folder(drive, name: str, parent: str | None, email: str, dry_run: bool) -> str:
    if dry_run:
        print(f"  [dry-run] folder «{name}» (parent={parent})")
        return f"dry-run-{name}"
    existing = find_folder(drive, name, parent)
    if existing:
        print(f"  ◐ folder «{name}» уже есть: {existing}")
        return existing
    body = {"name": name, "mimeType": "application/vnd.google-apps.folder"}
    if parent:
        body["parents"] = [parent]
    folder = drive.files().create(body=body, fields="id").execute()
    fid = folder["id"]
    if email:
        share(drive, fid, email, dry_run)
    return fid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", required=True, help="Путь к OAuth-токену пилота (b05-oauth-token.json)")
    ap.add_argument("--email", help="(устарело с OAuth-схемой — всё принадлежит пилоту)")
    ap.add_argument("--dry-run", action="store_true", help="Показать план без создания")
    args = ap.parse_args()

    sheets, drive = (None, None) if args.dry_run else make_services(args.token)

    manifest = {"created_by": "create-google-infra.py (WP-117 Ф1)", "farms": []}
    if args.dry_run:
        root_id = "dry-run-root"
    else:
        # корневая папка «B-05-visits» создана пилотом на его Диске;
        # всё внутри создаём от имени пилота (OAuth) — квота пилота
        root_id = find_folder(drive, ROOT_FOLDER_NAME, None)
        if not root_id:
            root_id = create_folder(drive, ROOT_FOLDER_NAME, None, None, dry_run=False)
    print(f"Корневая папка Drive: {root_id}")

    for farm in FARMS:
        print(f"Хозяйство: {farm['name']}")
        farm_folder = create_folder(drive, farm["name"], root_id, None, args.dry_run)
        sid = create_sheet(sheets, drive, farm, farm_folder, args.dry_run)
        subs = {s: create_folder(drive, s, farm_folder, None, args.dry_run)
                for s in DRIVE_SUBFOLDERS}
        manifest["farms"].append({
            **farm, "spreadsheet_id": sid, "drive_folder_id": farm_folder,
            "subfolders": subs,
        })

    if not args.dry_run:
        MANIFEST_PATH.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Манифест: {MANIFEST_PATH}")
    else:
        print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
