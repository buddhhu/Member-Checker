# Copyright Amit Sharma (https://github.com/buddhhu)

import sys

import requests
from decouple import config
from fastapi import FastAPI

BOT_TOKEN = config("BOT_TOKEN", default=None)

if not BOT_TOKEN:
    print("BOT_TOKEN missing.")
    sys.exit()

app = FastAPI()
base_url = f"https://api.telegram.org/bot{BOT_TOKEN}"


@app.get("/")
async def checker(chat_id: int, user_id: int):
    req = requests.get(
        f"{base_url}/getChatMember",
        params={"chat_id": chat_id, "user_id": user_id},
    ).json()
    if not req["ok"] and req["error_code"] == 400:
        requ = requests.get(f"{base_url}/getMe").json()
        req[
            "note"
        ] = f"Make sure you have added @{requ['result']['username']} in {chat_id}"
    return req
