from telegram import InlineKeyboardButton, InlineKeyboardMarkup

SOLO_PHOTO_ID = "AgACAgIAAxkBAAIBTGoAAYSMvTScmYSOFxvNxLTl5TLkoQAClBdrG9PHCUhDXoD8Lj4p1wEAAwIAA3kAAzsE"

SEASON_PHOTOS = {
    "solo_s1": "AgACAgIAAxkBAAIC4GoFW633bM-MdxuHG_IkzMhNvm7OAAJaEmsbX00pSCti6HtaNOLWAQADAgADeQADOwQ",
    "solo_s2": "AgACAgIAAxkBAAIC5GoFXeUqAsh9umxKkugfsw6k_tXHAAJhEmsbX00pSIkuXh7yUPLZAQADAgADeQADOwQ",
}
season_buttons = [
    [InlineKeyboardButton("📂 1 Сезон", callback_data="season1")],
    [InlineKeyboardButton("📂 2 Сезон", callback_data="season2")]
]

series_buttons = [
    [
        InlineKeyboardButton("🎬 1 Серия", callback_data="solo_ep1"),
        InlineKeyboardButton("🎬 2 Серия", callback_data="solo_ep2")
    ],
    [
        InlineKeyboardButton("🎬 3 Серия", callback_data="solo_ep3"),
        InlineKeyboardButton("🎬 4 Серия", callback_data="solo_ep4")
    ],
    [
        InlineKeyboardButton("🎬 5 Серия", callback_data="solo_ep5"),
        InlineKeyboardButton("🎬 6 Серия", callback_data="solo_ep6")
    ],
    [
        InlineKeyboardButton("🎬 7 Серия", callback_data="solo_ep7"),
        InlineKeyboardButton("🎬 8 Серия", callback_data="solo_ep8")
    ],
    [
        InlineKeyboardButton("🎬 9 Серия", callback_data="solo_ep9"),
        InlineKeyboardButton("🎬 10 Серия", callback_data="solo_ep10")
    ],
    [
        InlineKeyboardButton("🎬 11 Серия", callback_data="solo_ep11"),
        InlineKeyboardButton("🎬 12 Серия", callback_data="solo_ep12")
    ]
]

series_buttons2 = [
    [
        InlineKeyboardButton("🎬 1 Серия", callback_data="solo_s2ep1"),
        InlineKeyboardButton("🎬 2 Серия", callback_data="solo_s2ep2")
    ],
    [
        InlineKeyboardButton("🎬 3 Серия", callback_data="solo_s2ep3"),
        InlineKeyboardButton("🎬 4 Серия", callback_data="solo_s2ep4")
    ],
    [
        InlineKeyboardButton("🎬 5 Серия", callback_data="solo_s2ep5"),
        InlineKeyboardButton("🎬 6 Серия", callback_data="solo_s2ep6")
    ],
    [
        InlineKeyboardButton("🎬 7 Серия", callback_data="solo_s2ep7"),
        InlineKeyboardButton("🎬 8 Серия", callback_data="solo_s2ep8")
    ],
    [
        InlineKeyboardButton("🎬 9 Серия", callback_data="solo_s2ep9"),
        InlineKeyboardButton("🎬 10 Серия", callback_data="solo_s2ep10")
    ],
    [
        InlineKeyboardButton("🎬 11 Серия", callback_data="solo_s2ep11"),
        InlineKeyboardButton("🎬 12 Серия", callback_data="solo_s2ep12")
    ],
    [
        InlineKeyboardButton("🎬 13 Серия", callback_data="solo_s2ep13")
    ]
]

VIDEOS = {

    "solo_ep1": "BAACAgIAAxkBAAIB6WoCmhHLO2y-qi0edT6KZUs99oEdAAKnlwACNIMRSOAjORtND-ofOwQ",
    "solo_ep2": "BAACAgIAAxkBAAOdaf-74Sf0t9R3HQWAAZQn1hZq74sAAvKhAALMdwABSBAyecTjexzYOwQ",
    "solo_ep3": "BAACAgIAAxkBAAO1af_NhofFWgNyp46KQUGN0EWr7xYAAs6qAAK6yAFICKwZUbRHmxo7BA",
    "solo_ep4": "BAACAgIAAxkBAAO2af_N6wh8QEuLCrfOVSTDWwVchHQAAs-qAAK6yAFIKlEhEPgfIX87BA",
    "solo_ep5": "BAACAgIAAxkBAAO3af_OSFRG9Ba6JmRtaBhLktQ8TK4AAtCqAAK6yAFIAoLzSu-rvEM7BA",
    "solo_ep6": "BAACAgIAAxkBAAO4af_OppleRPYaUzAv4xE-JGpnQroAAtGqAAK6yAFI2E41OO1ekHA7BA",
    "solo_ep7": "BAACAgIAAxkBAAO5af_PLvJT3AW0cW99xXTAGwX8OvQAAtKqAAK6yAFIGt8niL7ub8M7BA",
    "solo_ep8": "BAACAgIAAxkBAAO6af_PjXvZWahQhdtBVh4NNi8ojw8AAtSqAAK6yAFIQ_zsnwZqcrQ7BA",
    "solo_ep9": "BAACAgIAAxkBAAO7af_QLzbN9XHjRFntZOZNgz259WEAAtWqAAK6yAFI9E3i4jFiMYA7BA",
    "solo_ep10": "BAACAgIAAxkBAAO8af_QkupmcAABsZHSSojohwpUzMpSAALWqgACusgBSNuuRLhFUwdGOwQ",
    "solo_ep11": "BAACAgIAAxkBAAO9af_QzUNCOo2BcKjjrl3G-XJ6gT4AAteqAAK6yAFI6XmYrT9IMd07BA",
    "solo_ep12": "BAACAgIAAxkBAAO-af_RDUyt0G3DyzExwAriMqO7uckAAtiqAAK6yAFIWqqAMwlp-Gc7BA",

    "solo_s2ep1": "BAACAgIAAxkBAAIB0WoB3VJ0hRkdf9vzoGcKHu6f3nq9AAIknwACNIMJSPBSgEBTgzw8OwQ",
    "solo_s2ep2": "BAACAgIAAxkBAAP5agABVTWRkZclr4pnm2KKHSuwrYBOAAKIowACusgJSBoyB67Gz3zSOwQ",
    "solo_s2ep3": "BAACAgIAAxkBAAP6agABVXepLS5qFVetLp-jDRdsPLfTAAKMowACusgJSN1UCBIuTpUOOwQ",
    "solo_s2ep4": "BAACAgIAAxkBAAP7agABVbvNi8nNIZSocOdX8GSIbkNEAAKVowACusgJSO7Q3pYV-_8oOwQ",
    "solo_s2ep5": "BAACAgIAAxkBAAP8agABVgSOTOc6wfJVmhnGPhIzMx1KAAKXowACusgJSGhcJK1VK2GROwQ",
    "solo_s2ep6": "BAACAgIAAxkBAAP9agABVn2p2im8EMgp6UioixfdKSMWAAKcowACusgJSPfmvqN2laatOwQ",
    "solo_s2ep7": "BAACAgIAAxkBAAP-agABVwABZth7_3nNXdhMx7tYpW8ShwACo6MAArrICUgnhd3nmIChnzsE",
    "solo_s2ep8": "BAACAgIAAxkBAAP_agABV7K63QgeQ9f5rgkY13hPIpaQAAKnowACusgJSCe7LGcDTMapOwQ",
    "solo_s2ep9": "BAACAgIAAxkBAAIBAAFqAAFYF3SYQt-fdM_GRoFTb25Mq_oAAq2jAAK6yAlIOLv7GGSU14w7BA",
    "solo_s2ep10": "BAACAgIAAxkBAAIBAWoAAVhax56rUjjpfROpcXBvgIbhygACsaMAArrICUj6TGYT9X0vRTsE",
    "solo_s2ep11": "BAACAgIAAxkBAAIBAmoAAVi33XUizeB6ESlWb_iNWu7TWgACuaMAArrICUgSOBbPKecoxTsE",
    "solo_s2ep12": "BAACAgIAAxkBAAIBA2oAAVkLAvB8SJE9gjtcNAaBu8NPNQACu6MAArrICUjpFJJx6unqLTsE",
    "solo_s2ep13": "BAACAgIAAxkBAAIBBGoAAVlWLS7yod0LmUN8C6Alm-sJDwACvKMAArrICUiCNslW_jrp4zsE"
}

PHOTO_ID = "AgACAgIAAxkBAAPeagABPb3YXP1O9k39ttOvAZa6OdQrAAKiF2sbusgJSL8WE8fHkqAXAQADAgADeQADOwQ"

CAPTIONS = {

    "solo_ep1": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep2": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep3": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep4": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep5": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep6": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep7": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep8": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep9": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep10": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep11": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "solo_ep12": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 1 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",

    "solo_s2ep1": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep2": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep3": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep4": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep5": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep6": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep7": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep8": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep9": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep10": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep11": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep12": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    "solo_s2ep13": "⚔️ Поднятие уровня в одиночку ⚔️\n\n📂 2 Сезон — 13 Серия\n\n🔥 Приятного просмотра!"
}

async def solo_menu(query, context):

    if query.data == "solo":

        await query.message.delete()

        await context.bot.send_photo(
    chat_id=query.message.chat_id,
    photo=SOLO_PHOTO_ID,
    caption="📂 Выбор сезон",
    reply_markup=InlineKeyboardMarkup(
        season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
    )
)

    elif query.data == "season1":

        await query.message.delete()

        await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=SEASON_PHOTOS["solo_s1"],
        caption="🎬 Выбор серия",
        reply_markup=InlineKeyboardMarkup(
            series_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_seasons")]]
        )
    )

    elif query.data == "season2":

        await query.message.delete()

        await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=SEASON_PHOTOS["solo_s2"],
        caption="🎬 Выбор серия",
        reply_markup=InlineKeyboardMarkup(
            series_buttons2 + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_seasons")]]
        )
    )

    elif query.data == "back_seasons":

        await query.message.delete()

        await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=SOLO_PHOTO_ID,
        caption="📂 Выбор сезон",
        reply_markup=InlineKeyboardMarkup(
            season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
        )
    )

    elif query.data == "close_anime":

        await query.message.delete()


    elif query.data == "close_series":

        await query.message.delete()

    elif query.data in VIDEOS:

        context.user_data["continue"] = query.data

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
