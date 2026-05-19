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

from solo import solo_menu
from titan import titan_menu
from rai import rai_menu


TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_USERNAME = "@anime_hubO7"

CATALOG_PHOTO_ID = "AgACAgIAAxkBAAIBWGoAAY2MGDmmO-Ua71NQ5vfPXNf2GAAC7hdrG9PHCUjM3_XCMr_poQEAAwIAA3kAAzsE"


anime_buttons = [
    [InlineKeyboardButton("⚔️ Поднятие уровня в одиночку", callback_data="solo")],
    [InlineKeyboardButton("🪽 Атака титанов", callback_data="titan")],
    [InlineKeyboardButton("🔥 Адский рай", callback_data="rai")]
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

    else:

        await solo_menu(query, context)


async def get_video(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.video and update.message.caption:

        file_id = update.message.video.file_id
        key = update.message.caption

        for filename in os.listdir():

            if filename.endswith(".py"):

                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()

                old = f'"{key}": "VIDEO_ID"'
                new = f'"{key}": "{file_id}"'

                if old in content:

                    content = content.replace(old, new)

                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(content)

                    print(f"\n✅ {key} ГОТОВО В {filename}\n")


async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.photo and update.message.caption:

        file_id = update.message.photo[-1].file_id
        key = update.message.caption

        for filename in os.listdir():

            if filename.endswith(".py"):

                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()

                old = f'"{key}": "PHOTO_ID"'
                new = f'"{key}": "{file_id}"'

                if old in content:

                    content = content.replace(old, new)

                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(content)

                    print(f"\n✅ {key} PHOTO ГОТОВО В {filename}\n")


app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.VIDEO, get_video))
app.add_handler(MessageHandler(filters.PHOTO, get_photo))

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("BOT STARTED")


flask_app = Flask(__name__)


@flask_app.route("/")
def home():
    return "Bot is running"


@flask_app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json(force=True)

    update = Update.de_json(data, app.bot)

    asyncio.run(app.initialize())
    asyncio.run(app.process_update(update))

    return "ok"