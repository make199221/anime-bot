<<<<<<< HEAD
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

SEASON_PHOTOS = {
    "demon_main": "AgACAgIAAxkBAAIEQWoMqEvL0IyczdkVqcK38CHMk41YAAI2G2sbmRJpSJG1TU1nsqCIAQADAgADeQADOwQ",
    "demon_s1": "PHOTO_ID",
    "demon_s2": "PHOTO_ID",
    "demon_s3": "PHOTO_ID",
    "demon_s4": "PHOTO_ID",
    "demon_s5": "PHOTO_ID"
}

season_buttons = [
    [InlineKeyboardButton("📂 1 Сезон", callback_data="demon_season1")],
    [InlineKeyboardButton("📂 2 Сезон", callback_data="demon_season2")],
    [InlineKeyboardButton("📂 3 Сезон", callback_data="demon_season3")],
    [InlineKeyboardButton("📂 4 Сезон", callback_data="demon_season4")],
    [InlineKeyboardButton("📂 5 Сезон", callback_data="demon_season5")]
]

season1_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="demon_s1ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="demon_s1ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="demon_s1ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="demon_s1ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="demon_s1ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="demon_s1ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="demon_s1ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="demon_s1ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="demon_s1ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="demon_s1ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="demon_s1ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="demon_s1ep12")],

    [InlineKeyboardButton("🎬 13 Серия", callback_data="demon_s1ep13"),
     InlineKeyboardButton("🎬 14 Серия", callback_data="demon_s1ep14")],

    [InlineKeyboardButton("🎬 15 Серия", callback_data="demon_s1ep15"),
     InlineKeyboardButton("🎬 16 Серия", callback_data="demon_s1ep16")],

    [InlineKeyboardButton("🎬 17 Серия", callback_data="demon_s1ep17"),
     InlineKeyboardButton("🎬 18 Серия", callback_data="demon_s1ep18")],

    [InlineKeyboardButton("🎬 19 Серия", callback_data="demon_s1ep19"),
     InlineKeyboardButton("🎬 20 Серия", callback_data="demon_s1ep20")],

    [InlineKeyboardButton("🎬 21 Серия", callback_data="demon_s1ep21"),
     InlineKeyboardButton("🎬 22 Серия", callback_data="demon_s1ep22")],

    [InlineKeyboardButton("🎬 23 Серия", callback_data="demon_s1ep23"),
     InlineKeyboardButton("🎬 24 Серия", callback_data="demon_s1ep24")],

    [InlineKeyboardButton("🎬 25 Серия", callback_data="demon_s1ep25"),
     InlineKeyboardButton("🎬 26 Серия", callback_data="demon_s1ep26")]
]

season2_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="demon_s2ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="demon_s2ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="demon_s2ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="demon_s2ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="demon_s2ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="demon_s2ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="demon_s2ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="demon_s2ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="demon_s2ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="demon_s2ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="demon_s2ep11")]
]

season3_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="demon_s3ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="demon_s3ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="demon_s3ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="demon_s3ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="demon_s3ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="demon_s3ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="demon_s3ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="demon_s3ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="demon_s3ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="demon_s3ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="demon_s3ep11")]
]

season4_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="demon_s4ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="demon_s4ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="demon_s4ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="demon_s4ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="demon_s4ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="demon_s4ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="demon_s4ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="demon_s4ep8")]
]

season5_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="demon_s5ep1")]
]

VIDEOS = {

    # ===== 1 СЕЗОН =====
    "demon_s1ep1": "VIDEO_ID",
    "demon_s1ep2": "VIDEO_ID",
    "demon_s1ep3": "VIDEO_ID",
    "demon_s1ep4": "VIDEO_ID",
    "demon_s1ep5": "VIDEO_ID",
    "demon_s1ep6": "VIDEO_ID",
    "demon_s1ep7": "VIDEO_ID",
    "demon_s1ep8": "VIDEO_ID",
    "demon_s1ep9": "VIDEO_ID",
    "demon_s1ep10": "VIDEO_ID",
    "demon_s1ep11": "VIDEO_ID",
    "demon_s1ep12": "VIDEO_ID",
    "demon_s1ep13": "VIDEO_ID",
    "demon_s1ep14": "VIDEO_ID",
    "demon_s1ep15": "VIDEO_ID",
    "demon_s1ep16": "VIDEO_ID",
    "demon_s1ep17": "VIDEO_ID",
    "demon_s1ep18": "VIDEO_ID",
    "demon_s1ep19": "VIDEO_ID",
    "demon_s1ep20": "VIDEO_ID",
    "demon_s1ep21": "VIDEO_ID",
    "demon_s1ep22": "VIDEO_ID",
    "demon_s1ep23": "VIDEO_ID",
    "demon_s1ep24": "VIDEO_ID",
    "demon_s1ep25": "VIDEO_ID",
    "demon_s1ep26": "VIDEO_ID",

    # ===== 2 СЕЗОН =====
    "demon_s2ep1": "VIDEO_ID",
    "demon_s2ep2": "VIDEO_ID",
    "demon_s2ep3": "VIDEO_ID",
    "demon_s2ep4": "VIDEO_ID",
    "demon_s2ep5": "VIDEO_ID",
    "demon_s2ep6": "VIDEO_ID",
    "demon_s2ep7": "VIDEO_ID",
    "demon_s2ep8": "VIDEO_ID",
    "demon_s2ep9": "VIDEO_ID",
    "demon_s2ep10": "VIDEO_ID",
    "demon_s2ep11": "VIDEO_ID",

    # ===== 3 СЕЗОН =====
    "demon_s3ep1": "VIDEO_ID",
    "demon_s3ep2": "VIDEO_ID",
    "demon_s3ep3": "VIDEO_ID",
    "demon_s3ep4": "VIDEO_ID",
    "demon_s3ep5": "VIDEO_ID",
    "demon_s3ep6": "VIDEO_ID",
    "demon_s3ep7": "VIDEO_ID",
    "demon_s3ep8": "VIDEO_ID",
    "demon_s3ep9": "VIDEO_ID",
    "demon_s3ep10": "VIDEO_ID",
    "demon_s3ep11": "VIDEO_ID",

    # ===== 4 СЕЗОН =====
    "demon_s4ep1": "VIDEO_ID",
    "demon_s4ep2": "VIDEO_ID",
    "demon_s4ep3": "VIDEO_ID",
    "demon_s4ep4": "VIDEO_ID",
    "demon_s4ep5": "VIDEO_ID",
    "demon_s4ep6": "VIDEO_ID",
    "demon_s4ep7": "VIDEO_ID",
    "demon_s4ep8": "VIDEO_ID",

    # ===== 5 СЕЗОН =====
    "demon_s5ep1": "VIDEO_ID",
}

CAPTIONS = {

    "demon_s1ep1": "🗡 Клинок рассекающих демонов\n\n📂 1 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "demon_s1ep2": "🗡 Клинок рассекающих демонов\n\n📂 1 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
}

async def demon_menu(query, context):

    if query.data == "demon":

            await query.message.delete()

            await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=SEASON_PHOTOS["demon_main"],
        caption="📂 Выбор сезон",
        reply_markup=InlineKeyboardMarkup(
            season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
        )
    )

    elif query.data == "demon_season1":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_s1"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season1_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="demon_back")]]
            )
        )

    elif query.data == "demon_season2":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_s2"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season2_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="demon_back")]]
            )
        )

    elif query.data == "demon_season3":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_s3"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season3_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="demon_back")]]
            )
        )

    elif query.data == "demon_season4":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_s4"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season4_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="demon_back")]]
            )
        )

    elif query.data == "demon_season5":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_s5"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season5_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="demon_back")]]
            )
        )

    elif query.data == "demon_back":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_main"],
            caption="📂 Выбор сезон",
            reply_markup=InlineKeyboardMarkup(
                season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
            )
        )

    elif query.data == "demon_close":

        await query.message.delete()

    elif query.data == "demon_close_series":

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
            caption=CAPTIONS.get(query.data, "🔥 Приятного просмотра!"),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ Закрыть", callback_data="demon_close_series")]
            ])
        )

=======
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

SEASON_PHOTOS = {
    "demon_main": "AgACAgIAAxkBAAIEQWoMqEvL0IyczdkVqcK38CHMk41YAAI2G2sbmRJpSJG1TU1nsqCIAQADAgADeQADOwQ",
    "demon_s1": "PHOTO_ID",
    "demon_s2": "PHOTO_ID",
    "demon_s3": "PHOTO_ID",
    "demon_s4": "PHOTO_ID",
    "demon_s5": "PHOTO_ID"
}

season_buttons = [
    [InlineKeyboardButton("📂 1 Сезон", callback_data="demon_season1")],
    [InlineKeyboardButton("📂 2 Сезон", callback_data="demon_season2")],
    [InlineKeyboardButton("📂 3 Сезон", callback_data="demon_season3")],
    [InlineKeyboardButton("📂 4 Сезон", callback_data="demon_season4")],
    [InlineKeyboardButton("📂 5 Сезон", callback_data="demon_season5")]
]

season1_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="demon_s1ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="demon_s1ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="demon_s1ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="demon_s1ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="demon_s1ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="demon_s1ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="demon_s1ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="demon_s1ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="demon_s1ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="demon_s1ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="demon_s1ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="demon_s1ep12")],

    [InlineKeyboardButton("🎬 13 Серия", callback_data="demon_s1ep13"),
     InlineKeyboardButton("🎬 14 Серия", callback_data="demon_s1ep14")],

    [InlineKeyboardButton("🎬 15 Серия", callback_data="demon_s1ep15"),
     InlineKeyboardButton("🎬 16 Серия", callback_data="demon_s1ep16")],

    [InlineKeyboardButton("🎬 17 Серия", callback_data="demon_s1ep17"),
     InlineKeyboardButton("🎬 18 Серия", callback_data="demon_s1ep18")],

    [InlineKeyboardButton("🎬 19 Серия", callback_data="demon_s1ep19"),
     InlineKeyboardButton("🎬 20 Серия", callback_data="demon_s1ep20")],

    [InlineKeyboardButton("🎬 21 Серия", callback_data="demon_s1ep21"),
     InlineKeyboardButton("🎬 22 Серия", callback_data="demon_s1ep22")],

    [InlineKeyboardButton("🎬 23 Серия", callback_data="demon_s1ep23"),
     InlineKeyboardButton("🎬 24 Серия", callback_data="demon_s1ep24")],

    [InlineKeyboardButton("🎬 25 Серия", callback_data="demon_s1ep25"),
     InlineKeyboardButton("🎬 26 Серия", callback_data="demon_s1ep26")]
]

season2_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="demon_s2ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="demon_s2ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="demon_s2ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="demon_s2ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="demon_s2ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="demon_s2ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="demon_s2ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="demon_s2ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="demon_s2ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="demon_s2ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="demon_s2ep11")]
]

season3_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="demon_s3ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="demon_s3ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="demon_s3ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="demon_s3ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="demon_s3ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="demon_s3ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="demon_s3ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="demon_s3ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="demon_s3ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="demon_s3ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="demon_s3ep11")]
]

season4_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="demon_s4ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="demon_s4ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="demon_s4ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="demon_s4ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="demon_s4ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="demon_s4ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="demon_s4ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="demon_s4ep8")]
]

season5_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="demon_s5ep1")]
]

VIDEOS = {

    # ===== 1 СЕЗОН =====
    "demon_s1ep1": "VIDEO_ID",
    "demon_s1ep2": "VIDEO_ID",
    "demon_s1ep3": "VIDEO_ID",
    "demon_s1ep4": "VIDEO_ID",
    "demon_s1ep5": "VIDEO_ID",
    "demon_s1ep6": "VIDEO_ID",
    "demon_s1ep7": "VIDEO_ID",
    "demon_s1ep8": "VIDEO_ID",
    "demon_s1ep9": "VIDEO_ID",
    "demon_s1ep10": "VIDEO_ID",
    "demon_s1ep11": "VIDEO_ID",
    "demon_s1ep12": "VIDEO_ID",
    "demon_s1ep13": "VIDEO_ID",
    "demon_s1ep14": "VIDEO_ID",
    "demon_s1ep15": "VIDEO_ID",
    "demon_s1ep16": "VIDEO_ID",
    "demon_s1ep17": "VIDEO_ID",
    "demon_s1ep18": "VIDEO_ID",
    "demon_s1ep19": "VIDEO_ID",
    "demon_s1ep20": "VIDEO_ID",
    "demon_s1ep21": "VIDEO_ID",
    "demon_s1ep22": "VIDEO_ID",
    "demon_s1ep23": "VIDEO_ID",
    "demon_s1ep24": "VIDEO_ID",
    "demon_s1ep25": "VIDEO_ID",
    "demon_s1ep26": "VIDEO_ID",

    # ===== 2 СЕЗОН =====
    "demon_s2ep1": "VIDEO_ID",
    "demon_s2ep2": "VIDEO_ID",
    "demon_s2ep3": "VIDEO_ID",
    "demon_s2ep4": "VIDEO_ID",
    "demon_s2ep5": "VIDEO_ID",
    "demon_s2ep6": "VIDEO_ID",
    "demon_s2ep7": "VIDEO_ID",
    "demon_s2ep8": "VIDEO_ID",
    "demon_s2ep9": "VIDEO_ID",
    "demon_s2ep10": "VIDEO_ID",
    "demon_s2ep11": "VIDEO_ID",

    # ===== 3 СЕЗОН =====
    "demon_s3ep1": "VIDEO_ID",
    "demon_s3ep2": "VIDEO_ID",
    "demon_s3ep3": "VIDEO_ID",
    "demon_s3ep4": "VIDEO_ID",
    "demon_s3ep5": "VIDEO_ID",
    "demon_s3ep6": "VIDEO_ID",
    "demon_s3ep7": "VIDEO_ID",
    "demon_s3ep8": "VIDEO_ID",
    "demon_s3ep9": "VIDEO_ID",
    "demon_s3ep10": "VIDEO_ID",
    "demon_s3ep11": "VIDEO_ID",

    # ===== 4 СЕЗОН =====
    "demon_s4ep1": "VIDEO_ID",
    "demon_s4ep2": "VIDEO_ID",
    "demon_s4ep3": "VIDEO_ID",
    "demon_s4ep4": "VIDEO_ID",
    "demon_s4ep5": "VIDEO_ID",
    "demon_s4ep6": "VIDEO_ID",
    "demon_s4ep7": "VIDEO_ID",
    "demon_s4ep8": "VIDEO_ID",

    # ===== 5 СЕЗОН =====
    "demon_s5ep1": "VIDEO_ID",
}

CAPTIONS = {

    "demon_s1ep1": "🗡 Клинок рассекающих демонов\n\n📂 1 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "demon_s1ep2": "🗡 Клинок рассекающих демонов\n\n📂 1 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
}

async def demon_menu(query, context):

    if query.data == "demon":

            await query.message.delete()

            await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=SEASON_PHOTOS["demon_main"],
        caption="📂 Выбор сезон",
        reply_markup=InlineKeyboardMarkup(
            season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
        )
    )

    elif query.data == "demon_season1":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_s1"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season1_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="demon_back")]]
            )
        )

    elif query.data == "demon_season2":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_s2"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season2_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="demon_back")]]
            )
        )

    elif query.data == "demon_season3":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_s3"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season3_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="demon_back")]]
            )
        )

    elif query.data == "demon_season4":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_s4"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season4_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="demon_back")]]
            )
        )

    elif query.data == "demon_season5":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_s5"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season5_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="demon_back")]]
            )
        )

    elif query.data == "demon_back":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["demon_main"],
            caption="📂 Выбор сезон",
            reply_markup=InlineKeyboardMarkup(
                season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
            )
        )

    elif query.data == "demon_close":

        await query.message.delete()

    elif query.data == "demon_close_series":

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
            caption=CAPTIONS.get(query.data, "🔥 Приятного просмотра!"),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❌ Закрыть", callback_data="demon_close_series")]
            ])
        )

>>>>>>> 0ce684e35d73729033b4f65cf6c877d8cb663463
        context.user_data["video_msg"] = msg.message_id