#!/usr/bin/env python3
"""oauth-authorize.py — WP-117: одноразовая OAuth-авторизация пилота (desktop flow).

Поднимает локальный приёмник на 127.0.0.1:8080, печатает ссылку авторизации,
принимает callback с кодом, обменивает его на токен и сохраняет
.secrets/b05-oauth-token.json (refresh token для контура B-05).

Использование: python3 oauth-authorize.py --client-secret /path/to/client_secret.json
"""
import argparse
import http.server
import json
import socketserver
import urllib.parse
import urllib.request

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
PORT = 8080
REDIRECT_HOST = "localhost"  # у клиента VS зарегистрирован redirect_uri http://localhost (не 127.0.0.1!)
TOKEN_PATH = "/home/asus/IWE/.secrets/b05-oauth-token.json"

auth_code = None
AUTH_URL = None


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        global auth_code
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        code = q.get("code", [None])[0]
        if code:
            auth_code = code
            self.send_response(200)
            self.end_headers()
            self.wfile.write("OK — можно закрыть вкладку и вернуться в чат.".encode())
        elif AUTH_URL:
            # нет кода — отдаём редирект на страницу авторизации Google
            self.send_response(302)
            self.send_header("Location", AUTH_URL)
            self.end_headers()
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(f"Ошибка: {q.get('error')}".encode())


def main():
    global AUTH_URL
    ap = argparse.ArgumentParser()
    ap.add_argument("--client-secret", required=True)
    args = ap.parse_args()

    with open(args.client_secret) as f:
        cs = json.load(f)["installed"]

    params = urllib.parse.urlencode({
        "client_id": cs["client_id"],
        "redirect_uri": f"http://localhost:{PORT}",
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
    })
    AUTH_URL = f"{cs['auth_uri']}?{params}"
    print(f"ССЫЛКА ДЛЯ АВТОРИЗАЦИИ:\n{AUTH_URL}\n", flush=True)

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Жду callback на localhost:{PORT} …", flush=True)
        while auth_code is None:
            httpd.handle_request()

    data = urllib.parse.urlencode({
        "code": auth_code,
        "client_id": cs["client_id"],
        "client_secret": cs["client_secret"],
        "redirect_uri": f"http://localhost:{PORT}",
        "grant_type": "authorization_code",
    }).encode()
    resp = urllib.request.urlopen(cs["token_uri"], data=data)
    token = json.load(resp)
    token["client_id"] = cs["client_id"]
    token["client_secret"] = cs["client_secret"]
    with open(TOKEN_PATH, "w") as f:
        json.dump(token, f, indent=2)
    print(f"✅ токен сохранён: {TOKEN_PATH} (refresh_token: {'есть' if 'refresh_token' in token else 'НЕТ!'})", flush=True)


if __name__ == "__main__":
    main()
