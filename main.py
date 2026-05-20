from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)

from flask import Flask, request

import asyncio
import os
import requests
import base64

from solo import solo_menu
from titan import titan_menu
from rai import rai_menu
from demon import demon_menu


TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_USERNAME = "@anime_hubO7"

CATALOG_PHOTO_ID = "AgACAgIAAxkBAAIBWGoAAY2MGDmmO-Ua71NQ5vfPXNf2GAAC7hdrG9PHCUjM3_XCMr_poQEAAwIAA3kAAzsE"


anime_buttons = [
    [InlineKeyboardButton("⚔️ Поднятие уровня в одиночку", callback_data="solo")],
    [InlineKeyboardButton("🪽 Атака титанов", callback_data="titan")],
    [InlineKeyboardButton("🔥 Адский рай", callback_data="rai")],
    [InlineKeyboardButton("🗡 Клинок рассекающих демонов", callback_data="demon")]
]


async def check_sub(user_id, context):

    member = await context.bot.get_chat_member(
        chat_id=CHANNEL_USERNAME,
        user_id=user_id
    )

    return member.status in ["member", "administrator", "creator"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not await check_sub(update.effective_user.id, context):

        await update.message.reply_photo(
            photo=CATALOG_PHOTO_ID,
            caption="❌ Для просмотра подпишитесь на канал!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📢 Подписаться", url="https://t.me/anime_hubO7")],
                [InlineKeyboardButton("✅ Проверить", callback_data="check_sub")]
            ])
        )

        return

    buttons_list = anime_buttons.copy()

    if "continue" in context.user_data:
        buttons_list.insert(0, [
            InlineKeyboardButton(
                "▶️ Продолжить просмотр",
                callback_data=context.user_data["continue"]
            )
        ])

    await update.message.reply_photo(
        photo=CATALOG_PHOTO_ID,
        caption="🍿 Каталог аниме",
        reply_markup=InlineKeyboardMarkup(buttons_list)
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "check_sub":

        if await check_sub(query.from_user.id, context):

            await query.message.delete()

            buttons_list = anime_buttons.copy()

            if "continue" in context.user_data:
                buttons_list.insert(0, [
                    InlineKeyboardButton(
                        "▶️ Продолжить просмотр",
                        callback_data=context.user_data["continue"]
                    )
                ])

            await context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=CATALOG_PHOTO_ID,
                caption="🍿 Каталог аниме",
                reply_markup=InlineKeyboardMarkup(buttons_list)
            )

        else:

            await query.answer("❌ Вы не подписаны!", show_alert=True)

        return

    if not await check_sub(query.from_user.id, context):

        await query.message.reply_photo(
            photo=CATALOG_PHOTO_ID,
            caption="❌ Для просмотра подпишитесь на канал!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📢 Подписаться", url="https://t.me/anime_hubO7")],
                [InlineKeyboardButton("✅ Проверить", callback_data="check_sub")]
            ])
        )

        return

    if query.data == "back_catalog":

        await query.message.delete()

        buttons_list = anime_buttons.copy()

        if "continue" in context.user_data:
            buttons_list.insert(0, [
                InlineKeyboardButton(
                    "▶️ Продолжить просмотр",
                    callback_data=context.user_data["continue"]
                )
            ])

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=CATALOG_PHOTO_ID,
            caption="🍿 Каталог аниме",
            reply_markup=InlineKeyboardMarkup(buttons_list)
        )

        return

    if query.data.startswith("titan"):

        await titan_menu(query, context)

    elif query.data.startswith("rai"):

        await rai_menu(query, context)

    elif query.data.startswith("demon"):

        await demon_menu(query, context)

    else:

        await solo_menu(query, context)


async def get_video(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.video and update.message.caption:

        print("\n🎬 VIDEO DETECTED")

        full_key = update.message.caption
        file_id = update.message.video.file_id

        print("FULL KEY:", full_key)
        print("VIDEO ID:", file_id)

        anime_file, key = full_key.split("|")

        py_file = f"{anime_file}.py"

        with open(py_file, "r", encoding="utf-8") as f:
            content = f.read()

        old = f'"{key}": "VIDEO_ID"'
        new = f'"{key}": "{file_id}"'

        content = content.replace(old, new)

        with open(py_file, "w", encoding="utf-8") as f:
            f.write(content)

        GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

        REPO = "make199221/anime-bot"

        url = f"https://api.github.com/repos/{REPO}/contents/{py_file}"

        headers = {
            "Authorization": f"token {GITHUB_TOKEN}"
        }

        r = requests.get(url, headers=headers)

        sha = r.json()["sha"]

        with open(py_file, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()

        data = {
            "message": f"auto update {key}",
            "content": encoded,
            "sha": sha
        }

        requests.put(url, headers=headers, json=data)

        print("✅ AUTO UPDATED:", key)


async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.photo and update.message.caption:

        print("\n🖼 PHOTO DETECTED")
        print("KEY:", update.message.caption)
        print("PHOTO ID:", update.message.photo[-1].file_id)
        print()


telegram_app = Application.builder().token(TOKEN).build()

telegram_app.add_handler(MessageHandler(filters.VIDEO, get_video))
telegram_app.add_handler(MessageHandler(filters.PHOTO, get_photo))

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CallbackQueryHandler(buttons))

print("BOT STARTED")


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

loop.run_until_complete(telegram_app.initialize())


flask_app = Flask(__name__)


@flask_app.route("/")
def home():
    return "Bot is running"


@flask_app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json(force=True)

    update = Update.de_json(data, telegram_app.bot)

    loop.run_until_complete(
        telegram_app.process_update(update)
    )

    return "ok"


app = flask_app