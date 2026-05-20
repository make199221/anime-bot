from telegram import InlineKeyboardButton, InlineKeyboardMarkup
SEASON_PHOTOS = {
    "rai_main": "AgACAgIAAxkBAAIDjWoFpsyMB3diCBxQrnz26k1iwYQNAAIyFGsbX00pSKnLrSIzjuUgAQADAgADeQADOwQ",
    "rai_s1": "AgACAgIAAxkBAAIDj2oFqHHSKIULk8nG2QABo_rR4WO_gQACPBRrG19NKUjSTj7SJkJjcgEAAwIAA3kAAzsE",
    "rai_s2": "AgACAgIAAxkBAAIDkGoFqQtfPvMeqAAByvV-HDALsbwGZAACSBRrG19NKUgBOlj3RP2BGwEAAwIAA3kAAzsE",
}

season_buttons = [
    [InlineKeyboardButton("📂 1 Сезон", callback_data="rai_season1")],
    [InlineKeyboardButton("📂 2 Сезон", callback_data="rai_season2")],
]

season1_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="rai_s1ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="rai_s1ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="rai_s1ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="rai_s1ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="rai_s1ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="rai_s1ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="rai_s1ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="rai_s1ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="rai_s1ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="rai_s1ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="rai_s1ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="rai_s1ep12")],

    [InlineKeyboardButton("🎬 13 Серия", callback_data="rai_s1ep13")],
]

season2_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="rai_s2ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="rai_s2ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="rai_s2ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="rai_s2ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="rai_s2ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="rai_s2ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="rai_s2ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="rai_s2ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="rai_s2ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="rai_s2ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="rai_s2ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="rai_s2ep12")],

]

VIDEOS = {
    # ===== 1 СЕЗОН =====
    "rai_s1ep1": "BAACAgIAAxkBAAIDjGoFoybkq0ZoM-h9gt-1OeIjcGPUAALrmgACX00pSA2DveGtA5KmOwQ",
    "rai_s1ep2": "BAACAgIAAxkBAAIDkmoFqlkTM2x2RZmjtnk-oY8cIFb4AAJOmwACX00pSKn7dGj7POg8OwQ",
    "rai_s1ep3": "BAACAgIAAxkBAAIDk2oFq14_xivEK3pESU_47_3jd7tsAAJjmwACX00pSGFLXCWf-j4hOwQ",
    "rai_s1ep4": "BAACAgIAAxkBAAIDo2oFsQ6XSb6Gt7Us32G47-nRDZTmAAKtmwACX00pSGzo9xFL2OleOwQ",
    "rai_s1ep5": "BAACAgIAAxkBAAIDpGoFseeY0SV0rllpQ97_s5VUN7TfAAK1mwACX00pSGZeG_4LJcc-OwQ",
    "rai_s1ep6": "BAACAgIAAxkBAAIDpWoFsrRl_ViFfPA7YOqFjJzvaGpLAALBmwACX00pSBEYCYQBUDdUOwQ",
    "rai_s1ep7": "BAACAgIAAxkBAAIDpmoFs2PJutysCLjImpPnGmroXb6aAALMmwACX00pSHncLaMqtwkMOwQ",
    "rai_s1ep8": "BAACAgIAAxkBAAIDp2oFtBvmRvhD1VI3CbmduP6HYOtiAALUmwACX00pSMpHxSj9ZEtiOwQ",
    "rai_s1ep9": "BAACAgIAAxkBAAIDqGoFtORtMEz_BqBb9PCJsQvzxG5wAALhmwACX00pSCamAdLqLNJhOwQ",
    "rai_s1ep10": "BAACAgIAAxkBAAIDqWoFtchRuYLl2ub6umNrK1pNOx_oAALqmwACX00pSOLJUkBaYGxIOwQ",
    "rai_s1ep11": "BAACAgIAAxkBAAIDqmoFtnablzI4tAMgqDl86MV7AAGJFAAC8ZsAAl9NKUhkyodSAAEYcyM7BA",
    "rai_s1ep12": "BAACAgIAAxkBAAIDq2oFuHuhWghNqHGFOF9aLvoImcfZAAILnAACX00pSIBpCAwu5JsGOwQ",
    "rai_s1ep13": "BAACAgIAAxkBAAIDrGoFu4su__pd-I_Pz9huXUfds5WkAAIunAACX00pSGk6omvlMQWXOwQ",

    # ===== 2 СЕЗОН =====
    "rai_s2ep1": "BAACAgIAAxkBAAID3moF7xzDkZKNMVJuw7ldAAEWX5Z6tAACvqEAAgWfMUiojXh0v0gsXjsE",
    "rai_s2ep2": "BAACAgIAAxkBAAID32oF7_Yf72i1whq7jhB2Xvm1E_P_AALJoQACBZ8xSG7mFGmqo5rqOwQ",
    "rai_s2ep3": "BAACAgIAAxkBAAID4GoF8D6lBF5pm43hnNfu_UEuMqQ0AALQoQACBZ8xSL2SLqJj6sLPOwQ",
    "rai_s2ep4": "BAACAgIAAxkBAAID4WoF9QwcJFxBT_d-8n65cb1KC_oFAAL6oQACBZ8xSKGe-I8AAcfgVjsE",
    "rai_s2ep5": "BAACAgIAAxkBAAID4moF9YDLyr4TFuSPEaWHrHnbRuqcAAIIogACBZ8xSM2Jh4jsL_inOwQ",
    "rai_s2ep6": "BAACAgIAAxkBAAID42oF9ufxohmt28HQxxLU7gliHxJIAAIcogACBZ8xSDXIuypFhuGqOwQ",
    "rai_s2ep7": "BAACAgIAAxkBAAID8GoGEygUZokKUFBhB0XONkZ7wsXgAAL_owACBZ8xSOnqkTEu0VOkOwQ",
    "rai_s2ep8": "BAACAgIAAxkBAAID9WoGF_jIID8CorfY5-hLMPrXNOFoAAJLpAACBZ8xSJ5j8bZR1IRNOwQ",
    "rai_s2ep9": "BAACAgIAAxkBAAID8WoGEzu4dGzgP-5L4B0PlJfi93HGAAIBpAACBZ8xSDIp7PTZmzp3OwQ",
    "rai_s2ep10": "BAACAgIAAxkBAAID9moGGI9XnQtEKZDip1J4jXuIwBDtAAJXpAACBZ8xSKAUySlqeUlMOwQ",
    "rai_s2ep11": "BAACAgIAAxkBAAID92oGGamVldO8ib8sHa3FSNQItgTsAAJrpAACBZ8xSKTK1qWvzbuvOwQ",
    "rai_s2ep12": "BAACAgIAAxkBAAID-GoGGawrBls1lbZ7p5Givmy0VT_4AAJspAACBZ8xSC7TLmnvPgHGOwQ",

}

CAPTIONS = {
    "rai_s1ep1": "🏝 Адский рай\n\n📂 1 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep2": "🏝 Адский рай\n\n📂 1 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep3": "🏝 Адский рай\n\n📂 1 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep4": "🏝 Адский рай\n\n📂 1 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep5": "🏝 Адский рай\n\n📂 1 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep6": "🏝 Адский рай\n\n📂 1 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep7": "🏝 Адский рай\n\n📂 1 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep8": "🏝 Адский рай\n\n📂 1 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep9": "🏝 Адский рай\n\n📂 1 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep10": "🏝 Адский рай\n\n📂 1 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep11": "🏝 Адский рай\n\n📂 1 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep12": "🏝 Адский рай\n\n📂 1 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    "rai_s1ep13": "🏝 Адский рай\n\n📂 1 Сезон — 13 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep1": "🏝 Адский рай\n\n📂 2 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep2": "🏝 Адский рай\n\n📂 2 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep3": "🏝 Адский рай\n\n📂 2 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep4": "🏝 Адский рай\n\n📂 2 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep5": "🏝 Адский рай\n\n📂 2 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep6": "🏝 Адский рай\n\n📂 2 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep7": "🏝 Адский рай\n\n📂 2 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep8": "🏝 Адский рай\n\n📂 2 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep9": "🏝 Адский рай\n\n📂 2 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep10": "🏝 Адский рай\n\n📂 2 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep11": "🏝 Адский рай\n\n📂 2 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "rai_s2ep12": "🏝 Адский рай\n\n📂 2 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
}

async def rai_menu(query, context):

    if query.data == "rai":

            await query.message.delete()

            await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=SEASON_PHOTOS["rai_main"],
        caption="📂 Выбор сезон",
        reply_markup=InlineKeyboardMarkup(
            season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
        )
    )

    elif query.data == "rai_season1":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["rai_s1"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season1_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="rai_back")]]
            )
        )

    elif query.data == "rai_season2":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["rai_s2"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season2_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="rai_back")]]
            )
        )

    elif query.data == "rai_back":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["rai_main"],
            caption="📂 Выбор сезон",
            reply_markup=InlineKeyboardMarkup(
                season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
            )
        )

    elif query.data == "rai_close":

        await query.message.delete()

    elif query.data == "rai_close_series":

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
                [InlineKeyboardButton("❌ Закрыть", callback_data="rai_close_series")]
            ])
        )

        context.user_data["video_msg"] = msg.message_id
