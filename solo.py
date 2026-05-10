from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8621683053:AAGzZzzyQ9B5oAKJMf3C1ZAC2azzjTaKsLA"

CATALOG_PHOTO_ID = "AgACAgIAAxkBAAIBWGoAAY2MGDmmO-Ua71NQ5vfPXNf2GAAC7hdrG9PHCUjM3_XCMr_poQEAAwIAA3kAAzsE"

SOLO_PHOTO_ID = "AgACAgIAAxkBAAIBTGoAAYSMvTScmYSOFxvNxLTl5TLkoQAClBdrG9PHCUhDXoD8Lj4p1wEAAwIAA3kAAzsE"

anime_buttons = [
    [InlineKeyboardButton("⚔️ Поднятие уровня в одиночку", callback_data="solo")]
]

season_buttons = [
    [InlineKeyboardButton("📂 1 Сезон", callback_data="season1")],
    [InlineKeyboardButton("📂 2 Сезон", callback_data="season2")]
]

series_buttons = [
    [
        InlineKeyboardButton("🎬 1 Серия", callback_data="ep1"),
        InlineKeyboardButton("🎬 2 Серия", callback_data="ep2")
    ],
    [
        InlineKeyboardButton("🎬 3 Серия", callback_data="ep3"),
        InlineKeyboardButton("🎬 4 Серия", callback_data="ep4")
    ],
    [
        InlineKeyboardButton("🎬 5 Серия", callback_data="ep5"),
        InlineKeyboardButton("🎬 6 Серия", callback_data="ep6")
    ],
    [
        InlineKeyboardButton("🎬 7 Серия", callback_data="ep7"),
        InlineKeyboardButton("🎬 8 Серия", callback_data="ep8")
    ],
    [
        InlineKeyboardButton("🎬 9 Серия", callback_data="ep9"),
        InlineKeyboardButton("🎬 10 Серия", callback_data="ep10")
    ],
    [
        InlineKeyboardButton("🎬 11 Серия", callback_data="ep11"),
        InlineKeyboardButton("🎬 12 Серия", callback_data="ep12")
    ]
]

series_buttons2 = [
    [
        InlineKeyboardButton("🎬 1 Серия", callback_data="s2ep1"),
        InlineKeyboardButton("🎬 2 Серия", callback_data="s2ep2")
    ],
    [
        InlineKeyboardButton("🎬 3 Серия", callback_data="s2ep3"),
        InlineKeyboardButton("🎬 4 Серия", callback_data="s2ep4")
    ],
    [
        InlineKeyboardButton("🎬 5 Серия", callback_data="s2ep5"),
        InlineKeyboardButton("🎬 6 Серия", callback_data="s2ep6")
    ],
    [
        InlineKeyboardButton("🎬 7 Серия", callback_data="s2ep7"),
        InlineKeyboardButton("🎬 8 Серия", callback_data="s2ep8")
    ],
    [
        InlineKeyboardButton("🎬 9 Серия", callback_data="s2ep9"),
        InlineKeyboardButton("🎬 10 Серия", callback_data="s2ep10")
    ],
    [
        InlineKeyboardButton("🎬 11 Серия", callback_data="s2ep11"),
        InlineKeyboardButton("🎬 12 Серия", callback_data="s2ep12")
    ],
    [
        InlineKeyboardButton("🎬 13 Серия", callback_data="s2ep13")
    ]
]

VIDEOS = {

    "ep1": "BAACAgIAAxkBAAOYaf-xXBJNCTZOovb2JYVoTOJivzsAAtehAALMdwABSGyZxHdOqXRnOwQ",
    "ep2": "BAACAgIAAxkBAAOdaf-74Sf0t9R3HQWAAZQn1hZq74sAAvKhAALMdwABSBAyecTjexzYOwQ",
    "ep3": "BAACAgIAAxkBAAO1af_NhofFWgNyp46KQUGN0EWr7xYAAs6qAAK6yAFICKwZUbRHmxo7BA",
    "ep4": "BAACAgIAAxkBAAO2af_N6wh8QEuLCrfOVSTDWwVchHQAAs-qAAK6yAFIKlEhEPgfIX87BA",
    "ep5": "BAACAgIAAxkBAAO3af_OSFRG9Ba6JmRtaBhLktQ8TK4AAtCqAAK6yAFIAoLzSu-rvEM7BA",
    "ep6": "BAACAgIAAxkBAAO4af_OppleRPYaUzAv4xE-JGpnQroAAtGqAAK6yAFI2E41OO1ekHA7BA",
    "ep7": "BAACAgIAAxkBAAO5af_PLvJT3AW0cW99xXTAGwX8OvQAAtKqAAK6yAFIGt8niL7ub8M7BA",
    "ep8": "BAACAgIAAxkBAAO6af_PjXvZWahQhdtBVh4NNi8ojw8AAtSqAAK6yAFIQ_zsnwZqcrQ7BA",
    "ep9": "BAACAgIAAxkBAAO7af_QLzbN9XHjRFntZOZNgz259WEAAtWqAAK6yAFI9E3i4jFiMYA7BA",
    "ep10": "BAACAgIAAxkBAAO8af_QkupmcAABsZHSSojohwpUzMpSAALWqgACusgBSNuuRLhFUwdGOwQ",
    "ep11": "BAACAgIAAxkBAAO9af_QzUNCOo2BcKjjrl3G-XJ6gT4AAteqAAK6yAFI6XmYrT9IMd07BA",
    "ep12": "BAACAgIAAxkBAAO-af_RDUyt0G3DyzExwAriMqO7uckAAtiqAAK6yAFIWqqAMwlp-Gc7BA",

    "s2ep1": "BAACAgIAAxkBAAP5agABVTWRkZclr4pnm2KKHSuwrYBOAAKIowACusgJSBoyB67Gz3zSOwQ",
    "s2ep2": "BAACAgIAAxkBAAP6agABVXepLS5qFVetLp-jDRdsPLfTAAKMowACusgJSN1UCBIuTpUOOwQ",
    "s2ep3": "BAACAgIAAxkBAAP7agABVbvNi8nNIZSocOdX8GSIbkNEAAKVowACusgJSO7Q3pYV-_8oOwQ",
    "s2ep4": "BAACAgIAAxkBAAP8agABVgSOTOc6wfJVmhnGPhIzMx1KAAKXowACusgJSGhcJK1VK2GROwQ",
    "s2ep5": "BAACAgIAAxkBAAP9agABVn2p2im8EMgp6UioixfdKSMWAAKcowACusgJSPfmvqN2laatOwQ",
    "s2ep6": "BAACAgIAAxkBAAP-agABVwABZth7_3nNXdhMx7tYpW8ShwACo6MAArrICUgnhd3nmIChnzsE",
    "s2ep7": "BAACAgIAAxkBAAP_agABV7K63QgeQ9f5rgkY13hPIpaQAAKnowACusgJSCe7LGcDTMapOwQ",
    "s2ep8": "BAACAgIAAxkBAAIBAAFqAAFYF3SYQt-fdM_GRoFTb25Mq_oAAq2jAAK6yAlIOLv7GGSU14w7BA",
    "s2ep9": "BAACAgIAAxkBAAIBAWoAAVhax56rUjjpfROpcXBvgIbhygACsaMAArrICUj6TGYT9X0vRTsE",
    "s2ep10": "BAACAgIAAxkBAAIBAmoAAVi33XUizeB6ESlWb_iNWu7TWgACuaMAArrICUgSOBbPKecoxTsE",
    "s2ep11": "BAACAgIAAxkBAAIBA2oAAVkLAvB8SJE9gjtcNAaBu8NPNQACu6MAArrICUjpFJJx6unqLTsE",
    "s2ep12": "BAACAgIAAxkBAAIBBGoAAVlWLS7yod0LmUN8C6Alm-sJDwACvKMAArrICUiCNslW_jrp4zsE",
    "s2ep13": "BAACAgIAAxkBAAIBBGoAAVlWLS7yod0LmUN8C6Alm-sJDwACvKMAArrICUiCNslW_jrp4zsE"
}

PHOTO_ID = "AgACAgIAAxkBAAPeagABPb3YXP1O9k39ttOvAZa6OdQrAAKiF2sbusgJSL8WE8fHkqAXAQADAgADeQADOwQ"

CAPTIONS = {

    "ep1": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "ep2": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "ep3": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "ep4": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "ep5": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "ep6": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "ep7": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "ep8": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "ep9": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "ep10": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "ep11": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "ep12": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",

    "s2ep1": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "s2ep2": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "s2ep3": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "s2ep4": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "s2ep5": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "s2ep6": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "s2ep7": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "s2ep8": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "s2ep9": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "s2ep10": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "s2ep11": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "s2ep12": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    "s2ep13": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 13 Серия\n\n🔥 Приятного просмотра!"

}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_photo(
        photo=CATALOG_PHOTO_ID,
        caption="🍿 Добро пожаловать в Anime Hub 🍿\n\n✨ Выберите аниме для просмотра ✨",
        reply_markup=InlineKeyboardMarkup(anime_buttons)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "solo":

        await query.message.delete()

        await context.bot.send_photo(
    chat_id=query.message.chat_id,
    photo=SOLO_PHOTO_ID,
    caption="📂 Выбор сезон",
    reply_markup=InlineKeyboardMarkup(
        season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="close_anime")]]
    )
)

    elif query.data == "season1":

        await query.message.edit_caption(
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                series_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_seasons")]]
            )
        )

    elif query.data == "season2":

        await query.message.edit_caption(
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                series_buttons2 + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_seasons")]]
            )
        )

    elif query.data == "back_seasons":

        await query.message.edit_caption(
            caption="📂 Выбор сезон",
            reply_markup=InlineKeyboardMarkup(
                season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="close_anime")]]
            )
        )

    elif query.data == "close_anime":

        await query.message.delete()

        await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=CATALOG_PHOTO_ID,
        caption="🍿 Добро пожаловать в Anime Hub 🍿\n\n✨ Выберите аниме для просмотра ✨",
        reply_markup=InlineKeyboardMarkup(anime_buttons)
    )

    elif query.data == "close_series":

        await query.message.delete()

    elif query.data in VIDEOS:

        if "video_msg" in context.user_data:
            try:
                await context.bot.delete_message(
                    chat_id=query.message.chat_id,
                    message_id=context.user_data["video_msg"]
                )
            except:
                pass

        msg = await context.bot.send_video(
            chat_id=query.message.chat_id,
            video=VIDEOS[query.data],
            caption=CAPTIONS[query.data],
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ Закрыть", callback_data="close_series")]
            ])
        )

        context.user_data["video_msg"] = msg.message_id

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("BOT STARTED")

app.run_polling()