<<<<<<< HEAD
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

SEASON_PHOTOS = {
    "titan_main": "AgACAgIAAxkBAAIC_WoFbP-PFdsvnaPSk58re9WZBB0LAAK2EmsbX00pSDI30_EKJD0KAQADAgADeQADOwQ",
    "titan_s1": "AgACAgIAAxkBAAIC9moFaT-ShtAxS-Ism5ytORgEHZmrAAKREmsbX00pSAk0dm0TWu_KAQADAgADeQADOwQ",
    "titan_s2": "AgACAgIAAxkBAAIC-moFa1WjqM7nBMANfWwhZ0VoEa16AAKjEmsbX00pSOYlEqEM-6IjAQADAgADeQADOwQ",
    "titan_s3": "AgACAgIAAxkBAAIC-2oFa54v11mb0PHmnMnxBPwfC1o5AAKtEmsbX00pSDJ_xTu_l4evAQADAgADeQADOwQ",
    "titan_s4": "AgACAgIAAxkBAAIC_GoFbF3JhN_EYi18jMxNRB1LU7qQAAKxEmsbX00pSEw-dyMAAUaq6AEAAwIAA3kAAzsE"
}

season_buttons = [
    [InlineKeyboardButton("📂 1 Сезон", callback_data="titan_season1")],
    [InlineKeyboardButton("📂 2 Сезон", callback_data="titan_season2")],
    [InlineKeyboardButton("📂 3 Сезон", callback_data="titan_season3")],
    [InlineKeyboardButton("📂 4 Сезон", callback_data="titan_season4")]
]

season1_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="titan_s1ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="titan_s1ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="titan_s1ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="titan_s1ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="titan_s1ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="titan_s1ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="titan_s1ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="titan_s1ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="titan_s1ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="titan_s1ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="titan_s1ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="titan_s1ep12")],

    [InlineKeyboardButton("🎬 13 Серия", callback_data="titan_s1ep13"),
     InlineKeyboardButton("🎬 14 Серия", callback_data="titan_s1ep14")],

    [InlineKeyboardButton("🎬 15 Серия", callback_data="titan_s1ep15"),
     InlineKeyboardButton("🎬 16 Серия", callback_data="titan_s1ep16")],

    [InlineKeyboardButton("🎬 17 Серия", callback_data="titan_s1ep17"),
     InlineKeyboardButton("🎬 18 Серия", callback_data="titan_s1ep18")],

    [InlineKeyboardButton("🎬 19 Серия", callback_data="titan_s1ep19"),
     InlineKeyboardButton("🎬 20 Серия", callback_data="titan_s1ep20")],

    [InlineKeyboardButton("🎬 21 Серия", callback_data="titan_s1ep21"),
     InlineKeyboardButton("🎬 22 Серия", callback_data="titan_s1ep22")],

    [InlineKeyboardButton("🎬 23 Серия", callback_data="titan_s1ep23"),
     InlineKeyboardButton("🎬 24 Серия", callback_data="titan_s1ep24")],

    [InlineKeyboardButton("🎬 25 Серия", callback_data="titan_s1ep25")]
]

season2_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="titan_s2ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="titan_s2ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="titan_s2ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="titan_s2ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="titan_s2ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="titan_s2ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="titan_s2ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="titan_s2ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="titan_s2ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="titan_s2ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="titan_s2ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="titan_s2ep12")]
]

season3_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="titan_s3ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="titan_s3ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="titan_s3ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="titan_s3ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="titan_s3ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="titan_s3ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="titan_s3ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="titan_s3ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="titan_s3ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="titan_s3ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="titan_s3ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="titan_s3ep12")],

    [InlineKeyboardButton("🎬 13 Серия", callback_data="titan_s3ep13"),
     InlineKeyboardButton("🎬 14 Серия", callback_data="titan_s3ep14")],

    [InlineKeyboardButton("🎬 15 Серия", callback_data="titan_s3ep15"),
     InlineKeyboardButton("🎬 16 Серия", callback_data="titan_s3ep16")],

    [InlineKeyboardButton("🎬 17 Серия", callback_data="titan_s3ep17"),
     InlineKeyboardButton("🎬 18 Серия", callback_data="titan_s3ep18")],

    [InlineKeyboardButton("🎬 19 Серия", callback_data="titan_s3ep19"),
     InlineKeyboardButton("🎬 20 Серия", callback_data="titan_s3ep20")],

    [InlineKeyboardButton("🎬 21 Серия", callback_data="titan_s3ep21"),
     InlineKeyboardButton("🎬 22 Серия", callback_data="titan_s3ep22")]
]

season4_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="titan_s4ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="titan_s4ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="titan_s4ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="titan_s4ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="titan_s4ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="titan_s4ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="titan_s4ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="titan_s4ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="titan_s4ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="titan_s4ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="titan_s4ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="titan_s4ep12")],

    [InlineKeyboardButton("🎬 13 Серия", callback_data="titan_s4ep13"),
     InlineKeyboardButton("🎬 14 Серия", callback_data="titan_s4ep14")],

    [InlineKeyboardButton("🎬 15 Серия", callback_data="titan_s4ep15"),
     InlineKeyboardButton("🎬 16 Серия", callback_data="titan_s4ep16")],

    [InlineKeyboardButton("🎬 17 Серия", callback_data="titan_s4ep17"),
     InlineKeyboardButton("🎬 18 Серия", callback_data="titan_s4ep18")],

    [InlineKeyboardButton("🎬 19 Серия", callback_data="titan_s4ep19"),
     InlineKeyboardButton("🎬 20 Серия", callback_data="titan_s4ep20")],

    [InlineKeyboardButton("🎬 21 Серия", callback_data="titan_s4ep21"),
     InlineKeyboardButton("🎬 22 Серия", callback_data="titan_s4ep22")],

    [InlineKeyboardButton("🎬 23 Серия", callback_data="titan_s4ep23"),
     InlineKeyboardButton("🎬 24 Серия", callback_data="titan_s4ep24")],

    [InlineKeyboardButton("🎬 25 Серия", callback_data="titan_s4ep25"),
     InlineKeyboardButton("🎬 26 Серия", callback_data="titan_s4ep26")],

    [InlineKeyboardButton("🎬 27 Серия", callback_data="titan_s4ep27"),
     InlineKeyboardButton("🎬 28 Серия", callback_data="titan_s4ep28")],

    [InlineKeyboardButton("🎬 29 Серия", callback_data="titan_s4ep29"),
     InlineKeyboardButton("🎬 30 Серия", callback_data="titan_s4ep30")],
]

VIDEOS = {

    # ===== 1 СЕЗОН =====
    "titan_s1ep1": "BAACAgIAAxkBAAICYGoC7tAkznhzjf7kGtL58km2YsKWAAJGmgACNIMRSLyNdJrHJIHOOwQ",
    "titan_s1ep2": "BAACAgIAAxkBAAICdGoDZ3Es-xwTZmSMintVWqoY0lcDAAJDoQACNIMZSDbpDzfTTBC8OwQ",
    "titan_s1ep3": "BAACAgIAAxkBAAICdWoDbAHcpH3I78KOPaH-UFrgv0o7AAJnoQACNIMZSEboXIOlyrIfOwQ",
    "titan_s1ep4": "BAACAgIAAxkBAAICdmoDbc1JHOqQUGJD8okBaPh4IaFvAAKPoQACNIMZSJ4zqFnW0tkOOwQ",
    "titan_s1ep5": "BAACAgIAAxkBAAICd2oDbzt4JKXNK83Yi6gwsBY_OqiQAAKkoQACNIMZSNsz14V18MiaOwQ",
    "titan_s1ep6": "BAACAgIAAxkBAAICgWoDccV4Fylfl352r556u5I9RzwyAALHoQACNIMZSOSNFPnGTPY1OwQ",
    "titan_s1ep7": "BAACAgIAAxkBAAICgmoDcjxjJOTMUG5VHCQZ7pvTcqwRAALRoQACNIMZSGDJTx3LOatROwQ",
    "titan_s1ep8": "BAACAgIAAxkBAAICg2oDcwZiBOZOEhRGIigJ0GqouUbqAALboQACNIMZSCieIURx8r01OwQ",
    "titan_s1ep9": "BAACAgIAAxkBAAIChGoDc2hMxSR46Fz0PQGSK_0mUghdAALjoQACNIMZSBh6V1PDvMTaOwQ",
    "titan_s1ep10": "BAACAgIAAxkBAAIChWoDdIn6vyxWaa4c08X-bjF3WDwwAAL1oQACNIMZSPsWRQSgH2M1OwQ",
    "titan_s1ep11": "BAACAgIAAxkBAAIChmoDdwMHHjnxzOq3KYmcOLh5EFdkAAIpogACNIMZSEtaVBG3JYOZOwQ",
    "titan_s1ep12": "BAACAgIAAxkBAAICh2oDeWkzrceyHDzpWNDSnG1NhDBUAAJEogACNIMZSBiI5x969I51OwQ",
    "titan_s1ep13": "BAACAgIAAxkBAAICiGoDex5quTZMD1DOkQPlhYU6SldzAAJXogACNIMZSEpJKyJvMSX7OwQ",
    "titan_s1ep14": "BAACAgIAAxkBAAICiWoDfiIQ7A2WnxKaqcJzJpQWO-6bAAJ3ogACNIMZSFpL481l-HLDOwQ",
    "titan_s1ep15": "BAACAgIAAxkBAAICimoDfz7aFrF85ZveBevYj5oQiOX7AAKGogACNIMZSDoV8TyhFkxhOwQ",
    "titan_s1ep16": "BAACAgIAAxkBAAICi2oDf8f0XkNiHYQHxOX34-9hUadAAAKSogACNIMZSP0RjRSh-l5JOwQ",
    "titan_s1ep17": "BAACAgIAAxkBAAICjGoDgM45hPokdqFAHOHMJR5qDFtcAAKdogACNIMZSNvY_XOPd7yWOwQ",
    "titan_s1ep18": "BAACAgIAAxkBAAICjWoDgfArgvlsVpppDBibFeD9XdS5AAKuogACNIMZSN2-rGege2Y8OwQ",
    "titan_s1ep19": "BAACAgIAAxkBAAICjmoDg2F38E-XZISqedbFe0Q91bOCAALGogACNIMZSLMU-3NLSUu3OwQ",
    "titan_s1ep20": "BAACAgIAAxkBAAICj2oDhMXm_V6ezF35VxZXaPVVrqGnAALvogACNIMZSMSEO1IB0PvqOwQ",
    "titan_s1ep21": "BAACAgIAAxkBAAICkGoDhdp2TnL-1uFhs_1rfGTcpgwsAAL8ogACNIMZSNwygcnYMgaXOwQ",
    "titan_s1ep22": "BAACAgIAAxkBAAICkWoDhrxSr2quhY44ioBOkYU6XmnCAAINowACNIMZSGRLkHDycB7BOwQ",
    "titan_s1ep23": "BAACAgIAAxkBAAICkmoDh5mWf5O9Fr7WxN67oqmxMiBnAAIZowACNIMZSMFZVCta-5eaOwQ",
    "titan_s1ep24": "BAACAgIAAxkBAAICk2oDiJopl2GYx3ORbDgZ5RsmojmUAAIhowACNIMZSAgPpQ-D-V_GOwQ",
    "titan_s1ep25": "BAACAgIAAxkBAAIClGoDidXNeUdjxnEDGwsIK3139wEhAAIrowACNIMZSHxAQ3-3NPMNOwQ",

    # ===== 2 СЕЗОН =====
    "titan_s2ep1": "BAACAgIAAxkBAAICnmoDjBkAAaRSn83qWtYCQmVYMtl4ewACRKMAAjSDGUiPQX2gIDjmzzsE",
    "titan_s2ep2": "BAACAgIAAxkBAAICn2oDjRQQgqxsVqpu9ZW-ATMMP2EFAAJQowACNIMZSNWAf1A-1Ds8OwQ",
    "titan_s2ep3": "BAACAgIAAxkBAAICoGoDjh5uGGdW8wGvpoe1GOSbYYPRAAJXowACNIMZSLMy0rfQI0_LOwQ",
    "titan_s2ep4": "BAACAgIAAxkBAAICoWoDjzA4m7Kuvxl4zoiWh4ANOkU_AAJeowACNIMZSGjWHhAqkpOdOwQ",
    "titan_s2ep5": "BAACAgIAAxkBAAIComoDj-NgXKjTgkGasctTFDbPwb5CAAJhowACNIMZSLh0XCfDUA_SOwQ",
    "titan_s2ep6": "BAACAgIAAxkBAAICo2oDkMjJmAYLOmLdfa2_7aynvaRGAAJpowACNIMZSEfTPEyliY1tOwQ",
    "titan_s2ep7": "BAACAgIAAxkBAAICpGoDkYGi4VZUSG-_BAUYOG7GM_OqAAJrowACNIMZSJe_2h2K3yGAOwQ",
    "titan_s2ep8": "BAACAgIAAxkBAAICpWoDkiWqqAUnaCkAATGiWBb-C2L9DgACbqMAAjSDGUiHzT8IPO6u_DsE",
    "titan_s2ep9": "BAACAgIAAxkBAAICpmoDktgI46mcs7EKXHf6ryu5yuKRAAJwowACNIMZSHKSzobTBBWBOwQ",
    "titan_s2ep10": "BAACAgIAAxkBAAICp2oDk5qfc-_zj-lK8nHxNTUbg6sdAAJzowACNIMZSLHARsdl9kbvOwQ",
    "titan_s2ep11": "BAACAgIAAxkBAAICqGoDlF0smrc6ZRZKUs3BA92s-1dGAAJ3owACNIMZSAx6853dm_kuOwQ",
    "titan_s2ep12": "BAACAgIAAxkBAAICqWoDlRc_Jj_McmNsQOXArDwQ2R9fAAJ6owACNIMZSC97BPr8agABZDsE",

    # ===== 3 СЕЗОН =====
    "titan_s3ep1": "BAACAgIAAxkBAAICq2oD_7AshLpaDSR2MuITEjxLoI2ZAAIUlQACX00hSMTAtVhY5hYROwQ",
    "titan_s3ep2": "BAACAgIAAxkBAAICrGoEAAEvdF77soHsraHEUKKeHvOb_QACF5UAAl9NIUjE-AUc9gGqyzsE",
    "titan_s3ep3": "BAACAgIAAxkBAAICrWoEAQe5-CaxGLr0S75sXqVLGCDEAAIelQACX00hSO7bcr6oOz1ROwQ",
    "titan_s3ep4": "BAACAgIAAxkBAAICrmoEAc8hgSRXCgK_NHCxfBiGV8X3AAIjlQACX00hSAROZfEY9bG7OwQ",
    "titan_s3ep5": "BAACAgIAAxkBAAICr2oEAuqnm0wXEjbAa3tRvtvW43bDAAIxlQACX00hSMlGsjI0QPpdOwQ",
    "titan_s3ep6": "BAACAgIAAxkBAAICsGoEA5-EOo1WE2hvStR7tDV9_ffdAAI4lQACX00hSF2svzYwglvDOwQ",
    "titan_s3ep7": "BAACAgIAAxkBAAICsWoEBDPaHu0Z8eOxJClFO7tgm9K7AAI9lQACX00hSHqhfkjBVhd7OwQ",
    "titan_s3ep8": "BAACAgIAAxkBAAICsmoEBUjUOQebYJ6wZTPm1XKFCgrSAAJElQACX00hSKjfQDWXWIbLOwQ",
    "titan_s3ep9": "BAACAgIAAxkBAAICs2oEBXzUEzXrWn-bScsB3OYqxCUtAAJHlQACX00hSJ3MHpBJshRlOwQ",
    "titan_s3ep10": "BAACAgIAAxkBAAICtGoEBjKwS8df-fRjVagAASp14dPyyQACSpUAAl9NIUhQgkKxMKYQCjsE",
    "titan_s3ep11": "BAACAgIAAxkBAAICtWoEBvdaHqp5R0EFU46sqHgvOAPkAAJUlQACX00hSKjux5E0k1i6OwQ",
    "titan_s3ep12": "BAACAgIAAxkBAAICtmoEB7F5JAMDph7iij-aTrDNRErGAAJalQACX00hSDO-Rd2Fh4qjOwQ",
    "titan_s3ep13": "BAACAgIAAxkBAAICt2oECLQyP8f8M4YuaMwvv5j6_U-6AAJilQACX00hSCA_x-IGkrZkOwQ",
    "titan_s3ep14": "BAACAgIAAxkBAAICvGoECZVR9FRl08RcGIl_J5piJT-jAAJplQACX00hSIjPjMHpR_VVOwQ",
    "titan_s3ep15": "BAACAgIAAxkBAAICvWoECkAZvHN6j7JTksKJeC3aZ_97AAJslQACX00hSH11-GQH7zHFOwQ",
    "titan_s3ep16": "BAACAgIAAxkBAAICvmoEC1G9ZSKZocaaXMxU29LxJn-4AAJzlQACX00hSH5mlsoKmvT_OwQ",
    "titan_s3ep17": "BAACAgIAAxkBAAICv2oEDTfgFgJh9JzRiZ1c70LtGUZ7AAKOlQACX00hSIUU0uNCR8FjOwQ",
    "titan_s3ep18": "BAACAgIAAxkBAAICwGoEDoG40sI8HCx3iUhahu6xKpi7AAKXlQACX00hSBz0spH7yiAiOwQ",
    "titan_s3ep19": "BAACAgIAAxkBAAICwWoED71kFTZ5K4DCyCxIxf6hvmj9AAKglQACX00hSBEhZi6b3UXPOwQ",
    "titan_s3ep20": "BAACAgIAAxkBAAICwmoEEykVpLQILrsLV_v-qHmlzNcYAALClQACX00hSGUkBfmIWJdzOwQ",
    "titan_s3ep21": "BAACAgIAAxkBAAICw2oEFXeaVc4HoEj0Q5kfJ0bodOt7AALZlQACX00hSJwzR23_d5JcOwQ",
    "titan_s3ep22": "BAACAgIAAxkBAAICxGoEF1G520xCn95fSbcpTtuCF4gaAALvlQACX00hSNgp1ImHaUiXOwQ",

    # ===== 4 СЕЗОН =====
    "titan_s4ep1": "BAACAgIAAxkBAAICxWoEOGiiAaM002eXKwNSnAMXoS2bAAIvlwACX00hSJfjq19XlvfQOwQ",
    "titan_s4ep2": "BAACAgIAAxkBAAICxmoEOiRJ_x1Xf9MXvoWoHt1X_2UZAAJNlwACX00hSGaa60vU-PokOwQ",
    "titan_s4ep3": "BAACAgIAAxkBAAICx2oEO2z8iXN6t9oMRJ5jgst6cA3aAAJilwACX00hSIIWR--vHJecOwQ",
    "titan_s4ep4": "BAACAgIAAxkBAAICyGoEPPuucgRklvvoD4fCWFvtcTDPAAJ_lwACX00hSKVzl1fFJhvUOwQ",
    "titan_s4ep5": "BAACAgIAAxkBAAICyWoEPo7bggbaibyHAAH1q1sAAVrkJSwAApiXAAJfTSFI2seYVDcYU647BA",
    "titan_s4ep6": "BAACAgIAAxkBAAICymoEQREWl4a9k26dinFk1gN77mfcAAK2lwACX00hSKi1deI5_lKwOwQ",
    "titan_s4ep7": "BAACAgIAAxkBAAICy2oEQqFN1uWopl4ds5kKTkjFyiMzAALMlwACX00hSOgfbMQCd5BDOwQ",
    "titan_s4ep8": "BAACAgIAAxkBAAICzGoEREKEVmtmaBsP9-M8fCo4hcNIAALolwACX00hSJ-_3Asjmq-3OwQ",
    "titan_s4ep9": "BAACAgIAAxkBAAICzWoERZzbexRctVqDikffXmcjYaFXAAL8lwACX00hSBJiMc2fxB8qOwQ",
    "titan_s4ep10": "BAACAgIAAxkBAAICzmoERx_-UP4asqy2KW0nmGCzEJNxAAIGmAACX00hSLF-Sy8AAaKlATsE",
    "titan_s4ep11": "BAACAgIAAxkBAAICz2oESLZxd9EztrDNzSn7wm6nOIMHAAISmAACX00hSBe1CcBsVwLkOwQ",
    "titan_s4ep12": "BAACAgIAAxkBAAIC0WoEVHXaAAEGHDCMmjXhXBChz7tYLAACvJgAAl9NIUg1BcMXG10k4jsE",
    "titan_s4ep13": "BAACAgIAAxkBAAIC7GoFYyt6CrLz5fNUZB_iDNk_ipbWAAL1mAACX00pSB9OVGLFM5UdOwQ",
    "titan_s4ep14": "BAACAgIAAxkBAAIC1moEsMwOetOB1dIffh3WHm8eJ3hGAAIMnwACX00hSDkLNjSDQpSLOwQ",
    "titan_s4ep15": "BAACAgIAAxkBAAIDFmoFcW_BVeo8tVqc9c7gfd6bG23FAAJCmQACX00pSL8Ehw_91yopOwQ",
    "titan_s4ep16": "BAACAgIAAxkBAAIDF2oFdBjxJJJjlxtgiPDOj9gLsuLTAAJPmQACX00pSPIxqF-HTimNOwQ",
    "titan_s4ep17": "BAACAgIAAxkBAAIDGGoFdMpth8srpGapIx_2wfJagQIPAAJYmQACX00pSC_BCn7lq8XoOwQ",
    "titan_s4ep18": "BAACAgIAAxkBAAIDGWoFdVHiLOh-cGw4muQb15tRDf1FAAJemQACX00pSLfJomJ0HWniOwQ",
    "titan_s4ep19": "BAACAgIAAxkBAAIDGmoFdqJdL2Il80FfIKzzvGdgu_uvAAJkmQACX00pSFn8soN6luTgOwQ",
    "titan_s4ep20": "BAACAgIAAxkBAAIDG2oFd0RzgSOWS-WJyNyO_6Z3nPc3AAJqmQACX00pSCdSFWjuK9GUOwQ",
    "titan_s4ep21": "BAACAgIAAxkBAAIDHGoFd8PdD2nde92gOwQY_nFWJ4IpAAJtmQACX00pSLRqL_uaVIhLOwQ",
    "titan_s4ep22": "BAACAgIAAxkBAAIDHWoFePMvFuttl_VRu7hxN4vM2E8VAAJ4mQACX00pSF5c7hfvlkkTOwQ",
    "titan_s4ep23": "BAACAgIAAxkBAAIDHmoFeZCuP-viN4me_KBl494XbbE-AAJ7mQACX00pSJxC5sYzqey4OwQ",
    "titan_s4ep24": "BAACAgIAAxkBAAIDH2oFehYexhEZcSLaqICkzO4-qy5cAAJ-mQACX00pSCOfchrbP8PVOwQ",
    "titan_s4ep25": "BAACAgIAAxkBAAIDIGoFey0BP5dAit8JWYXMoRnUAoFsAAKJmQACX00pSEjEegMyhzlUOwQ",
    "titan_s4ep26": "BAACAgIAAxkBAAIDIWoFe5l6HjP2BvNSQEu7rhmie0eAAAKLmQACX00pSOeO7PnjuH-3OwQ",
    "titan_s4ep27": "BAACAgIAAxkBAAIDImoFfVIdI-Y8jEx_lPvCt94CTAVjAAKOmQACX00pSIl4jCvdZBl6OwQ",
    "titan_s4ep28": "BAACAgIAAxkBAAIDI2oFfk9gm_YeDWgLKV2yXneMsyk4AAKSmQACX00pSP7fMopSC3IsOwQ",
    "titan_s4ep29": "BAACAgIAAxkBAAIDJGoFf4_U_mjhe8Yk3ieuwowjvzjEAAKkmQACX00pSHQ8xdlf32BaOwQ",
    "titan_s4ep30": "BAACAgIAAxkBAAIDMmoFhE2lpso6FiRoAuh0Vskdtf9IAALRmQACX00pSEyMttQhuF5fOwQ",
}

CAPTIONS = {
    "titan_s1ep1": "🪽 Атака титанов\n\n📂 1 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep2": "🪽 Атака титанов\n\n📂 1 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep3": "🪽 Атака титанов\n\n📂 1 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep4": "🪽 Атака титанов\n\n📂 1 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep5": "🪽 Атака титанов\n\n📂 1 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep6": "🪽 Атака титанов\n\n📂 1 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep7": "🪽 Атака титанов\n\n📂 1 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep8": "🪽 Атака титанов\n\n📂 1 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep9": "🪽 Атака титанов\n\n📂 1 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep10": "🪽 Атака титанов\n\n📂 1 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep11": "🪽 Атака титанов\n\n📂 1 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep12": "🪽 Атака титанов\n\n📂 1 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep13": "🪽 Атака титанов\n\n📂 1 Сезон — 13 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep14": "🪽 Атака титанов\n\n📂 1 Сезон — 14 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep15": "🪽 Атака титанов\n\n📂 1 Сезон — 15 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep16": "🪽 Атака титанов\n\n📂 1 Сезон — 16 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep17": "🪽 Атака титанов\n\n📂 1 Сезон — 17 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep18": "🪽 Атака титанов\n\n📂 1 Сезон — 18 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep19": "🪽 Атака титанов\n\n📂 1 Сезон — 19 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep20": "🪽 Атака титанов\n\n📂 1 Сезон — 20 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep21": "🪽 Атака титанов\n\n📂 1 Сезон — 21 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep22": "🪽 Атака титанов\n\n📂 1 Сезон — 22 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep23": "🪽 Атака титанов\n\n📂 1 Сезон — 23 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep24": "🪽 Атака титанов\n\n📂 1 Сезон — 24 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep25": "🪽 Атака титанов\n\n📂 1 Сезон — 25 Серия\n\n🔥 Приятного просмотра!",

    "titan_s2ep1": "🪽 Атака титанов\n\n📂 2 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep2": "🪽 Атака титанов\n\n📂 2 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep3": "🪽 Атака титанов\n\n📂 2 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep4": "🪽 Атака титанов\n\n📂 2 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep5": "🪽 Атака титанов\n\n📂 2 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep6": "🪽 Атака титанов\n\n📂 2 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep7": "🪽 Атака титанов\n\n📂 2 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep8": "🪽 Атака титанов\n\n📂 2 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep9": "🪽 Атака титанов\n\n📂 2 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep10": "🪽 Атака титанов\n\n📂 2 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep11": "🪽 Атака титанов\n\n📂 2 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep12": "🪽 Атака титанов\n\n📂 2 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    
    "titan_s3ep1": "🪽 Атака титанов\n\n📂 3 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep2": "🪽 Атака титанов\n\n📂 3 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep3": "🪽 Атака титанов\n\n📂 3 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep4": "🪽 Атака титанов\n\n📂 3 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep5": "🪽 Атака титанов\n\n📂 3 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep6": "🪽 Атака титанов\n\n📂 3 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep7": "🪽 Атака титанов\n\n📂 3 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep8": "🪽 Атака титанов\n\n📂 3 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep9": "🪽 Атака титанов\n\n📂 3 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep10": "🪽 Атака титанов\n\n📂 3 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep11": "🪽 Атака титанов\n\n📂 3 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep12": "🪽 Атака титанов\n\n📂 3 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep13": "🪽 Атака титанов\n\n📂 3 Сезон — 13 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep14": "🪽 Атака титанов\n\n📂 3 Сезон — 14 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep15": "🪽 Атака титанов\n\n📂 3 Сезон — 15 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep16": "🪽 Атака титанов\n\n📂 3 Сезон — 16 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep17": "🪽 Атака титанов\n\n📂 3 Сезон — 17 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep18": "🪽 Атака титанов\n\n📂 3 Сезон — 18 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep19": "🪽 Атака титанов\n\n📂 3 Сезон — 19 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep20": "🪽 Атака титанов\n\n📂 3 Сезон — 20 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep21": "🪽 Атака титанов\n\n📂 3 Сезон — 21 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep22": "🪽 Атака титанов\n\n📂 3 Сезон — 22 Серия\n\n🔥 Приятного просмотра!",

    "titan_s4ep1": "🪽 Атака титанов\n\n📂 4 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep2": "🪽 Атака титанов\n\n📂 4 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep3": "🪽 Атака титанов\n\n📂 4 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep4": "🪽 Атака титанов\n\n📂 4 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep5": "🪽 Атака титанов\n\n📂 4 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep6": "🪽 Атака титанов\n\n📂 4 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep7": "🪽 Атака титанов\n\n📂 4 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep8": "🪽 Атака титанов\n\n📂 4 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep9": "🪽 Атака титанов\n\n📂 4 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep10": "🪽 Атака титанов\n\n📂 4 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep11": "🪽 Атака титанов\n\n📂 4 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep12": "🪽 Атака титанов\n\n📂 4 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep13": "🪽 Атака титанов\n\n📂 4 Сезон — 13 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep14": "🪽 Атака титанов\n\n📂 4 Сезон — 14 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep15": "🪽 Атака титанов\n\n📂 4 Сезон — 15 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep16": "🪽 Атака титанов\n\n📂 4 Сезон — 16 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep17": "🪽 Атака титанов\n\n📂 4 Сезон — 17 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep18": "🪽 Атака титанов\n\n📂 4 Сезон — 18 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep19": "🪽 Атака титанов\n\n📂 4 Сезон — 19 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep20": "🪽 Атака титанов\n\n📂 4 Сезон — 20 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep21": "🪽 Атака титанов\n\n📂 4 Сезон — 21 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep22": "🪽 Атака титанов\n\n📂 4 Сезон — 22 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep23": "🪽 Атака титанов\n\n📂 4 Сезон — 23 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep24": "🪽 Атака титанов\n\n📂 4 Сезон — 24 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep25": "🪽 Атака титанов\n\n📂 4 Сезон — 25 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep26": "🪽 Атака титанов\n\n📂 4 Сезон — 26 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep27": "🪽 Атака титанов\n\n📂 4 Сезон — 27 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep28": "🪽 Атака титанов\n\n📂 4 Сезон — 28 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep29": "🪽 Атака титанов\n\n📂 4 Сезон — 29 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep30": "🪽 Атака титанов\n\n📂 4 Сезон — 30 Серия\n\n🔥 Приятного просмотра!",
}

async def titan_menu(query, context):

    if query.data == "titan":

            await query.message.delete()

            await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=SEASON_PHOTOS["titan_main"],
        caption="📂 Выбор сезон",
        reply_markup=InlineKeyboardMarkup(
            season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
        )
    )

    elif query.data == "titan_season1":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["titan_s1"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season1_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="titan_back")]]
            )
        )

    elif query.data == "titan_season2":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["titan_s2"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season2_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="titan_back")]]
            )
        )

    elif query.data == "titan_season3":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["titan_s3"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season3_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="titan_back")]]
            )
        )

    elif query.data == "titan_season4":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["titan_s4"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season4_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="titan_back")]]
            )
        )

    elif query.data == "titan_back":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["titan_main"],
            caption="📂 Выбор сезон",
            reply_markup=InlineKeyboardMarkup(
                season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
            )
        )

    elif query.data == "titan_close":

        await query.message.delete()

    elif query.data == "titan_close_series":

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
                [InlineKeyboardButton("❌ Закрыть", callback_data="titan_close_series")]
            ])
        )

=======
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

SEASON_PHOTOS = {
    "titan_main": "AgACAgIAAxkBAAIC_WoFbP-PFdsvnaPSk58re9WZBB0LAAK2EmsbX00pSDI30_EKJD0KAQADAgADeQADOwQ",
    "titan_s1": "AgACAgIAAxkBAAIC9moFaT-ShtAxS-Ism5ytORgEHZmrAAKREmsbX00pSAk0dm0TWu_KAQADAgADeQADOwQ",
    "titan_s2": "AgACAgIAAxkBAAIC-moFa1WjqM7nBMANfWwhZ0VoEa16AAKjEmsbX00pSOYlEqEM-6IjAQADAgADeQADOwQ",
    "titan_s3": "AgACAgIAAxkBAAIC-2oFa54v11mb0PHmnMnxBPwfC1o5AAKtEmsbX00pSDJ_xTu_l4evAQADAgADeQADOwQ",
    "titan_s4": "AgACAgIAAxkBAAIC_GoFbF3JhN_EYi18jMxNRB1LU7qQAAKxEmsbX00pSEw-dyMAAUaq6AEAAwIAA3kAAzsE"
}

season_buttons = [
    [InlineKeyboardButton("📂 1 Сезон", callback_data="titan_season1")],
    [InlineKeyboardButton("📂 2 Сезон", callback_data="titan_season2")],
    [InlineKeyboardButton("📂 3 Сезон", callback_data="titan_season3")],
    [InlineKeyboardButton("📂 4 Сезон", callback_data="titan_season4")]
]

season1_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="titan_s1ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="titan_s1ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="titan_s1ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="titan_s1ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="titan_s1ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="titan_s1ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="titan_s1ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="titan_s1ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="titan_s1ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="titan_s1ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="titan_s1ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="titan_s1ep12")],

    [InlineKeyboardButton("🎬 13 Серия", callback_data="titan_s1ep13"),
     InlineKeyboardButton("🎬 14 Серия", callback_data="titan_s1ep14")],

    [InlineKeyboardButton("🎬 15 Серия", callback_data="titan_s1ep15"),
     InlineKeyboardButton("🎬 16 Серия", callback_data="titan_s1ep16")],

    [InlineKeyboardButton("🎬 17 Серия", callback_data="titan_s1ep17"),
     InlineKeyboardButton("🎬 18 Серия", callback_data="titan_s1ep18")],

    [InlineKeyboardButton("🎬 19 Серия", callback_data="titan_s1ep19"),
     InlineKeyboardButton("🎬 20 Серия", callback_data="titan_s1ep20")],

    [InlineKeyboardButton("🎬 21 Серия", callback_data="titan_s1ep21"),
     InlineKeyboardButton("🎬 22 Серия", callback_data="titan_s1ep22")],

    [InlineKeyboardButton("🎬 23 Серия", callback_data="titan_s1ep23"),
     InlineKeyboardButton("🎬 24 Серия", callback_data="titan_s1ep24")],

    [InlineKeyboardButton("🎬 25 Серия", callback_data="titan_s1ep25")]
]

season2_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="titan_s2ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="titan_s2ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="titan_s2ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="titan_s2ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="titan_s2ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="titan_s2ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="titan_s2ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="titan_s2ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="titan_s2ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="titan_s2ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="titan_s2ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="titan_s2ep12")]
]

season3_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="titan_s3ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="titan_s3ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="titan_s3ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="titan_s3ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="titan_s3ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="titan_s3ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="titan_s3ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="titan_s3ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="titan_s3ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="titan_s3ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="titan_s3ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="titan_s3ep12")],

    [InlineKeyboardButton("🎬 13 Серия", callback_data="titan_s3ep13"),
     InlineKeyboardButton("🎬 14 Серия", callback_data="titan_s3ep14")],

    [InlineKeyboardButton("🎬 15 Серия", callback_data="titan_s3ep15"),
     InlineKeyboardButton("🎬 16 Серия", callback_data="titan_s3ep16")],

    [InlineKeyboardButton("🎬 17 Серия", callback_data="titan_s3ep17"),
     InlineKeyboardButton("🎬 18 Серия", callback_data="titan_s3ep18")],

    [InlineKeyboardButton("🎬 19 Серия", callback_data="titan_s3ep19"),
     InlineKeyboardButton("🎬 20 Серия", callback_data="titan_s3ep20")],

    [InlineKeyboardButton("🎬 21 Серия", callback_data="titan_s3ep21"),
     InlineKeyboardButton("🎬 22 Серия", callback_data="titan_s3ep22")]
]

season4_buttons = [
    [InlineKeyboardButton("🎬 1 Серия", callback_data="titan_s4ep1"),
     InlineKeyboardButton("🎬 2 Серия", callback_data="titan_s4ep2")],

    [InlineKeyboardButton("🎬 3 Серия", callback_data="titan_s4ep3"),
     InlineKeyboardButton("🎬 4 Серия", callback_data="titan_s4ep4")],

    [InlineKeyboardButton("🎬 5 Серия", callback_data="titan_s4ep5"),
     InlineKeyboardButton("🎬 6 Серия", callback_data="titan_s4ep6")],

    [InlineKeyboardButton("🎬 7 Серия", callback_data="titan_s4ep7"),
     InlineKeyboardButton("🎬 8 Серия", callback_data="titan_s4ep8")],

    [InlineKeyboardButton("🎬 9 Серия", callback_data="titan_s4ep9"),
     InlineKeyboardButton("🎬 10 Серия", callback_data="titan_s4ep10")],

    [InlineKeyboardButton("🎬 11 Серия", callback_data="titan_s4ep11"),
     InlineKeyboardButton("🎬 12 Серия", callback_data="titan_s4ep12")],

    [InlineKeyboardButton("🎬 13 Серия", callback_data="titan_s4ep13"),
     InlineKeyboardButton("🎬 14 Серия", callback_data="titan_s4ep14")],

    [InlineKeyboardButton("🎬 15 Серия", callback_data="titan_s4ep15"),
     InlineKeyboardButton("🎬 16 Серия", callback_data="titan_s4ep16")],

    [InlineKeyboardButton("🎬 17 Серия", callback_data="titan_s4ep17"),
     InlineKeyboardButton("🎬 18 Серия", callback_data="titan_s4ep18")],

    [InlineKeyboardButton("🎬 19 Серия", callback_data="titan_s4ep19"),
     InlineKeyboardButton("🎬 20 Серия", callback_data="titan_s4ep20")],

    [InlineKeyboardButton("🎬 21 Серия", callback_data="titan_s4ep21"),
     InlineKeyboardButton("🎬 22 Серия", callback_data="titan_s4ep22")],

    [InlineKeyboardButton("🎬 23 Серия", callback_data="titan_s4ep23"),
     InlineKeyboardButton("🎬 24 Серия", callback_data="titan_s4ep24")],

    [InlineKeyboardButton("🎬 25 Серия", callback_data="titan_s4ep25"),
     InlineKeyboardButton("🎬 26 Серия", callback_data="titan_s4ep26")],

    [InlineKeyboardButton("🎬 27 Серия", callback_data="titan_s4ep27"),
     InlineKeyboardButton("🎬 28 Серия", callback_data="titan_s4ep28")],

    [InlineKeyboardButton("🎬 29 Серия", callback_data="titan_s4ep29"),
     InlineKeyboardButton("🎬 30 Серия", callback_data="titan_s4ep30")],
]

VIDEOS = {

    # ===== 1 СЕЗОН =====
    "titan_s1ep1": "BAACAgIAAxkBAAICYGoC7tAkznhzjf7kGtL58km2YsKWAAJGmgACNIMRSLyNdJrHJIHOOwQ",
    "titan_s1ep2": "BAACAgIAAxkBAAICdGoDZ3Es-xwTZmSMintVWqoY0lcDAAJDoQACNIMZSDbpDzfTTBC8OwQ",
    "titan_s1ep3": "BAACAgIAAxkBAAICdWoDbAHcpH3I78KOPaH-UFrgv0o7AAJnoQACNIMZSEboXIOlyrIfOwQ",
    "titan_s1ep4": "BAACAgIAAxkBAAICdmoDbc1JHOqQUGJD8okBaPh4IaFvAAKPoQACNIMZSJ4zqFnW0tkOOwQ",
    "titan_s1ep5": "BAACAgIAAxkBAAICd2oDbzt4JKXNK83Yi6gwsBY_OqiQAAKkoQACNIMZSNsz14V18MiaOwQ",
    "titan_s1ep6": "BAACAgIAAxkBAAICgWoDccV4Fylfl352r556u5I9RzwyAALHoQACNIMZSOSNFPnGTPY1OwQ",
    "titan_s1ep7": "BAACAgIAAxkBAAICgmoDcjxjJOTMUG5VHCQZ7pvTcqwRAALRoQACNIMZSGDJTx3LOatROwQ",
    "titan_s1ep8": "BAACAgIAAxkBAAICg2oDcwZiBOZOEhRGIigJ0GqouUbqAALboQACNIMZSCieIURx8r01OwQ",
    "titan_s1ep9": "BAACAgIAAxkBAAIChGoDc2hMxSR46Fz0PQGSK_0mUghdAALjoQACNIMZSBh6V1PDvMTaOwQ",
    "titan_s1ep10": "BAACAgIAAxkBAAIChWoDdIn6vyxWaa4c08X-bjF3WDwwAAL1oQACNIMZSPsWRQSgH2M1OwQ",
    "titan_s1ep11": "BAACAgIAAxkBAAIChmoDdwMHHjnxzOq3KYmcOLh5EFdkAAIpogACNIMZSEtaVBG3JYOZOwQ",
    "titan_s1ep12": "BAACAgIAAxkBAAICh2oDeWkzrceyHDzpWNDSnG1NhDBUAAJEogACNIMZSBiI5x969I51OwQ",
    "titan_s1ep13": "BAACAgIAAxkBAAICiGoDex5quTZMD1DOkQPlhYU6SldzAAJXogACNIMZSEpJKyJvMSX7OwQ",
    "titan_s1ep14": "BAACAgIAAxkBAAICiWoDfiIQ7A2WnxKaqcJzJpQWO-6bAAJ3ogACNIMZSFpL481l-HLDOwQ",
    "titan_s1ep15": "BAACAgIAAxkBAAICimoDfz7aFrF85ZveBevYj5oQiOX7AAKGogACNIMZSDoV8TyhFkxhOwQ",
    "titan_s1ep16": "BAACAgIAAxkBAAICi2oDf8f0XkNiHYQHxOX34-9hUadAAAKSogACNIMZSP0RjRSh-l5JOwQ",
    "titan_s1ep17": "BAACAgIAAxkBAAICjGoDgM45hPokdqFAHOHMJR5qDFtcAAKdogACNIMZSNvY_XOPd7yWOwQ",
    "titan_s1ep18": "BAACAgIAAxkBAAICjWoDgfArgvlsVpppDBibFeD9XdS5AAKuogACNIMZSN2-rGege2Y8OwQ",
    "titan_s1ep19": "BAACAgIAAxkBAAICjmoDg2F38E-XZISqedbFe0Q91bOCAALGogACNIMZSLMU-3NLSUu3OwQ",
    "titan_s1ep20": "BAACAgIAAxkBAAICj2oDhMXm_V6ezF35VxZXaPVVrqGnAALvogACNIMZSMSEO1IB0PvqOwQ",
    "titan_s1ep21": "BAACAgIAAxkBAAICkGoDhdp2TnL-1uFhs_1rfGTcpgwsAAL8ogACNIMZSNwygcnYMgaXOwQ",
    "titan_s1ep22": "BAACAgIAAxkBAAICkWoDhrxSr2quhY44ioBOkYU6XmnCAAINowACNIMZSGRLkHDycB7BOwQ",
    "titan_s1ep23": "BAACAgIAAxkBAAICkmoDh5mWf5O9Fr7WxN67oqmxMiBnAAIZowACNIMZSMFZVCta-5eaOwQ",
    "titan_s1ep24": "BAACAgIAAxkBAAICk2oDiJopl2GYx3ORbDgZ5RsmojmUAAIhowACNIMZSAgPpQ-D-V_GOwQ",
    "titan_s1ep25": "BAACAgIAAxkBAAIClGoDidXNeUdjxnEDGwsIK3139wEhAAIrowACNIMZSHxAQ3-3NPMNOwQ",

    # ===== 2 СЕЗОН =====
    "titan_s2ep1": "BAACAgIAAxkBAAICnmoDjBkAAaRSn83qWtYCQmVYMtl4ewACRKMAAjSDGUiPQX2gIDjmzzsE",
    "titan_s2ep2": "BAACAgIAAxkBAAICn2oDjRQQgqxsVqpu9ZW-ATMMP2EFAAJQowACNIMZSNWAf1A-1Ds8OwQ",
    "titan_s2ep3": "BAACAgIAAxkBAAICoGoDjh5uGGdW8wGvpoe1GOSbYYPRAAJXowACNIMZSLMy0rfQI0_LOwQ",
    "titan_s2ep4": "BAACAgIAAxkBAAICoWoDjzA4m7Kuvxl4zoiWh4ANOkU_AAJeowACNIMZSGjWHhAqkpOdOwQ",
    "titan_s2ep5": "BAACAgIAAxkBAAIComoDj-NgXKjTgkGasctTFDbPwb5CAAJhowACNIMZSLh0XCfDUA_SOwQ",
    "titan_s2ep6": "BAACAgIAAxkBAAICo2oDkMjJmAYLOmLdfa2_7aynvaRGAAJpowACNIMZSEfTPEyliY1tOwQ",
    "titan_s2ep7": "BAACAgIAAxkBAAICpGoDkYGi4VZUSG-_BAUYOG7GM_OqAAJrowACNIMZSJe_2h2K3yGAOwQ",
    "titan_s2ep8": "BAACAgIAAxkBAAICpWoDkiWqqAUnaCkAATGiWBb-C2L9DgACbqMAAjSDGUiHzT8IPO6u_DsE",
    "titan_s2ep9": "BAACAgIAAxkBAAICpmoDktgI46mcs7EKXHf6ryu5yuKRAAJwowACNIMZSHKSzobTBBWBOwQ",
    "titan_s2ep10": "BAACAgIAAxkBAAICp2oDk5qfc-_zj-lK8nHxNTUbg6sdAAJzowACNIMZSLHARsdl9kbvOwQ",
    "titan_s2ep11": "BAACAgIAAxkBAAICqGoDlF0smrc6ZRZKUs3BA92s-1dGAAJ3owACNIMZSAx6853dm_kuOwQ",
    "titan_s2ep12": "BAACAgIAAxkBAAICqWoDlRc_Jj_McmNsQOXArDwQ2R9fAAJ6owACNIMZSC97BPr8agABZDsE",

    # ===== 3 СЕЗОН =====
    "titan_s3ep1": "BAACAgIAAxkBAAICq2oD_7AshLpaDSR2MuITEjxLoI2ZAAIUlQACX00hSMTAtVhY5hYROwQ",
    "titan_s3ep2": "BAACAgIAAxkBAAICrGoEAAEvdF77soHsraHEUKKeHvOb_QACF5UAAl9NIUjE-AUc9gGqyzsE",
    "titan_s3ep3": "BAACAgIAAxkBAAICrWoEAQe5-CaxGLr0S75sXqVLGCDEAAIelQACX00hSO7bcr6oOz1ROwQ",
    "titan_s3ep4": "BAACAgIAAxkBAAICrmoEAc8hgSRXCgK_NHCxfBiGV8X3AAIjlQACX00hSAROZfEY9bG7OwQ",
    "titan_s3ep5": "BAACAgIAAxkBAAICr2oEAuqnm0wXEjbAa3tRvtvW43bDAAIxlQACX00hSMlGsjI0QPpdOwQ",
    "titan_s3ep6": "BAACAgIAAxkBAAICsGoEA5-EOo1WE2hvStR7tDV9_ffdAAI4lQACX00hSF2svzYwglvDOwQ",
    "titan_s3ep7": "BAACAgIAAxkBAAICsWoEBDPaHu0Z8eOxJClFO7tgm9K7AAI9lQACX00hSHqhfkjBVhd7OwQ",
    "titan_s3ep8": "BAACAgIAAxkBAAICsmoEBUjUOQebYJ6wZTPm1XKFCgrSAAJElQACX00hSKjfQDWXWIbLOwQ",
    "titan_s3ep9": "BAACAgIAAxkBAAICs2oEBXzUEzXrWn-bScsB3OYqxCUtAAJHlQACX00hSJ3MHpBJshRlOwQ",
    "titan_s3ep10": "BAACAgIAAxkBAAICtGoEBjKwS8df-fRjVagAASp14dPyyQACSpUAAl9NIUhQgkKxMKYQCjsE",
    "titan_s3ep11": "BAACAgIAAxkBAAICtWoEBvdaHqp5R0EFU46sqHgvOAPkAAJUlQACX00hSKjux5E0k1i6OwQ",
    "titan_s3ep12": "BAACAgIAAxkBAAICtmoEB7F5JAMDph7iij-aTrDNRErGAAJalQACX00hSDO-Rd2Fh4qjOwQ",
    "titan_s3ep13": "BAACAgIAAxkBAAICt2oECLQyP8f8M4YuaMwvv5j6_U-6AAJilQACX00hSCA_x-IGkrZkOwQ",
    "titan_s3ep14": "BAACAgIAAxkBAAICvGoECZVR9FRl08RcGIl_J5piJT-jAAJplQACX00hSIjPjMHpR_VVOwQ",
    "titan_s3ep15": "BAACAgIAAxkBAAICvWoECkAZvHN6j7JTksKJeC3aZ_97AAJslQACX00hSH11-GQH7zHFOwQ",
    "titan_s3ep16": "BAACAgIAAxkBAAICvmoEC1G9ZSKZocaaXMxU29LxJn-4AAJzlQACX00hSH5mlsoKmvT_OwQ",
    "titan_s3ep17": "BAACAgIAAxkBAAICv2oEDTfgFgJh9JzRiZ1c70LtGUZ7AAKOlQACX00hSIUU0uNCR8FjOwQ",
    "titan_s3ep18": "BAACAgIAAxkBAAICwGoEDoG40sI8HCx3iUhahu6xKpi7AAKXlQACX00hSBz0spH7yiAiOwQ",
    "titan_s3ep19": "BAACAgIAAxkBAAICwWoED71kFTZ5K4DCyCxIxf6hvmj9AAKglQACX00hSBEhZi6b3UXPOwQ",
    "titan_s3ep20": "BAACAgIAAxkBAAICwmoEEykVpLQILrsLV_v-qHmlzNcYAALClQACX00hSGUkBfmIWJdzOwQ",
    "titan_s3ep21": "BAACAgIAAxkBAAICw2oEFXeaVc4HoEj0Q5kfJ0bodOt7AALZlQACX00hSJwzR23_d5JcOwQ",
    "titan_s3ep22": "BAACAgIAAxkBAAICxGoEF1G520xCn95fSbcpTtuCF4gaAALvlQACX00hSNgp1ImHaUiXOwQ",

    # ===== 4 СЕЗОН =====
    "titan_s4ep1": "BAACAgIAAxkBAAICxWoEOGiiAaM002eXKwNSnAMXoS2bAAIvlwACX00hSJfjq19XlvfQOwQ",
    "titan_s4ep2": "BAACAgIAAxkBAAICxmoEOiRJ_x1Xf9MXvoWoHt1X_2UZAAJNlwACX00hSGaa60vU-PokOwQ",
    "titan_s4ep3": "BAACAgIAAxkBAAICx2oEO2z8iXN6t9oMRJ5jgst6cA3aAAJilwACX00hSIIWR--vHJecOwQ",
    "titan_s4ep4": "BAACAgIAAxkBAAICyGoEPPuucgRklvvoD4fCWFvtcTDPAAJ_lwACX00hSKVzl1fFJhvUOwQ",
    "titan_s4ep5": "BAACAgIAAxkBAAICyWoEPo7bggbaibyHAAH1q1sAAVrkJSwAApiXAAJfTSFI2seYVDcYU647BA",
    "titan_s4ep6": "BAACAgIAAxkBAAICymoEQREWl4a9k26dinFk1gN77mfcAAK2lwACX00hSKi1deI5_lKwOwQ",
    "titan_s4ep7": "BAACAgIAAxkBAAICy2oEQqFN1uWopl4ds5kKTkjFyiMzAALMlwACX00hSOgfbMQCd5BDOwQ",
    "titan_s4ep8": "BAACAgIAAxkBAAICzGoEREKEVmtmaBsP9-M8fCo4hcNIAALolwACX00hSJ-_3Asjmq-3OwQ",
    "titan_s4ep9": "BAACAgIAAxkBAAICzWoERZzbexRctVqDikffXmcjYaFXAAL8lwACX00hSBJiMc2fxB8qOwQ",
    "titan_s4ep10": "BAACAgIAAxkBAAICzmoERx_-UP4asqy2KW0nmGCzEJNxAAIGmAACX00hSLF-Sy8AAaKlATsE",
    "titan_s4ep11": "BAACAgIAAxkBAAICz2oESLZxd9EztrDNzSn7wm6nOIMHAAISmAACX00hSBe1CcBsVwLkOwQ",
    "titan_s4ep12": "BAACAgIAAxkBAAIC0WoEVHXaAAEGHDCMmjXhXBChz7tYLAACvJgAAl9NIUg1BcMXG10k4jsE",
    "titan_s4ep13": "BAACAgIAAxkBAAIC7GoFYyt6CrLz5fNUZB_iDNk_ipbWAAL1mAACX00pSB9OVGLFM5UdOwQ",
    "titan_s4ep14": "BAACAgIAAxkBAAIC1moEsMwOetOB1dIffh3WHm8eJ3hGAAIMnwACX00hSDkLNjSDQpSLOwQ",
    "titan_s4ep15": "BAACAgIAAxkBAAIDFmoFcW_BVeo8tVqc9c7gfd6bG23FAAJCmQACX00pSL8Ehw_91yopOwQ",
    "titan_s4ep16": "BAACAgIAAxkBAAIDF2oFdBjxJJJjlxtgiPDOj9gLsuLTAAJPmQACX00pSPIxqF-HTimNOwQ",
    "titan_s4ep17": "BAACAgIAAxkBAAIDGGoFdMpth8srpGapIx_2wfJagQIPAAJYmQACX00pSC_BCn7lq8XoOwQ",
    "titan_s4ep18": "BAACAgIAAxkBAAIDGWoFdVHiLOh-cGw4muQb15tRDf1FAAJemQACX00pSLfJomJ0HWniOwQ",
    "titan_s4ep19": "BAACAgIAAxkBAAIDGmoFdqJdL2Il80FfIKzzvGdgu_uvAAJkmQACX00pSFn8soN6luTgOwQ",
    "titan_s4ep20": "BAACAgIAAxkBAAIDG2oFd0RzgSOWS-WJyNyO_6Z3nPc3AAJqmQACX00pSCdSFWjuK9GUOwQ",
    "titan_s4ep21": "BAACAgIAAxkBAAIDHGoFd8PdD2nde92gOwQY_nFWJ4IpAAJtmQACX00pSLRqL_uaVIhLOwQ",
    "titan_s4ep22": "BAACAgIAAxkBAAIDHWoFePMvFuttl_VRu7hxN4vM2E8VAAJ4mQACX00pSF5c7hfvlkkTOwQ",
    "titan_s4ep23": "BAACAgIAAxkBAAIDHmoFeZCuP-viN4me_KBl494XbbE-AAJ7mQACX00pSJxC5sYzqey4OwQ",
    "titan_s4ep24": "BAACAgIAAxkBAAIDH2oFehYexhEZcSLaqICkzO4-qy5cAAJ-mQACX00pSCOfchrbP8PVOwQ",
    "titan_s4ep25": "BAACAgIAAxkBAAIDIGoFey0BP5dAit8JWYXMoRnUAoFsAAKJmQACX00pSEjEegMyhzlUOwQ",
    "titan_s4ep26": "BAACAgIAAxkBAAIDIWoFe5l6HjP2BvNSQEu7rhmie0eAAAKLmQACX00pSOeO7PnjuH-3OwQ",
    "titan_s4ep27": "BAACAgIAAxkBAAIDImoFfVIdI-Y8jEx_lPvCt94CTAVjAAKOmQACX00pSIl4jCvdZBl6OwQ",
    "titan_s4ep28": "BAACAgIAAxkBAAIDI2oFfk9gm_YeDWgLKV2yXneMsyk4AAKSmQACX00pSP7fMopSC3IsOwQ",
    "titan_s4ep29": "BAACAgIAAxkBAAIDJGoFf4_U_mjhe8Yk3ieuwowjvzjEAAKkmQACX00pSHQ8xdlf32BaOwQ",
    "titan_s4ep30": "BAACAgIAAxkBAAIDMmoFhE2lpso6FiRoAuh0Vskdtf9IAALRmQACX00pSEyMttQhuF5fOwQ",
}

CAPTIONS = {
    "titan_s1ep1": "🪽 Атака титанов\n\n📂 1 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep2": "🪽 Атака титанов\n\n📂 1 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep3": "🪽 Атака титанов\n\n📂 1 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep4": "🪽 Атака титанов\n\n📂 1 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep5": "🪽 Атака титанов\n\n📂 1 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep6": "🪽 Атака титанов\n\n📂 1 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep7": "🪽 Атака титанов\n\n📂 1 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep8": "🪽 Атака титанов\n\n📂 1 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep9": "🪽 Атака титанов\n\n📂 1 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep10": "🪽 Атака титанов\n\n📂 1 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep11": "🪽 Атака титанов\n\n📂 1 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep12": "🪽 Атака титанов\n\n📂 1 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep13": "🪽 Атака титанов\n\n📂 1 Сезон — 13 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep14": "🪽 Атака титанов\n\n📂 1 Сезон — 14 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep15": "🪽 Атака титанов\n\n📂 1 Сезон — 15 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep16": "🪽 Атака титанов\n\n📂 1 Сезон — 16 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep17": "🪽 Атака титанов\n\n📂 1 Сезон — 17 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep18": "🪽 Атака титанов\n\n📂 1 Сезон — 18 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep19": "🪽 Атака титанов\n\n📂 1 Сезон — 19 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep20": "🪽 Атака титанов\n\n📂 1 Сезон — 20 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep21": "🪽 Атака титанов\n\n📂 1 Сезон — 21 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep22": "🪽 Атака титанов\n\n📂 1 Сезон — 22 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep23": "🪽 Атака титанов\n\n📂 1 Сезон — 23 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep24": "🪽 Атака титанов\n\n📂 1 Сезон — 24 Серия\n\n🔥 Приятного просмотра!",
    "titan_s1ep25": "🪽 Атака титанов\n\n📂 1 Сезон — 25 Серия\n\n🔥 Приятного просмотра!",

    "titan_s2ep1": "🪽 Атака титанов\n\n📂 2 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep2": "🪽 Атака титанов\n\n📂 2 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep3": "🪽 Атака титанов\n\n📂 2 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep4": "🪽 Атака титанов\n\n📂 2 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep5": "🪽 Атака титанов\n\n📂 2 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep6": "🪽 Атака титанов\n\n📂 2 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep7": "🪽 Атака титанов\n\n📂 2 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep8": "🪽 Атака титанов\n\n📂 2 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep9": "🪽 Атака титанов\n\n📂 2 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep10": "🪽 Атака титанов\n\n📂 2 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep11": "🪽 Атака титанов\n\n📂 2 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "titan_s2ep12": "🪽 Атака титанов\n\n📂 2 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    
    "titan_s3ep1": "🪽 Атака титанов\n\n📂 3 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep2": "🪽 Атака титанов\n\n📂 3 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep3": "🪽 Атака титанов\n\n📂 3 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep4": "🪽 Атака титанов\n\n📂 3 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep5": "🪽 Атака титанов\n\n📂 3 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep6": "🪽 Атака титанов\n\n📂 3 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep7": "🪽 Атака титанов\n\n📂 3 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep8": "🪽 Атака титанов\n\n📂 3 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep9": "🪽 Атака титанов\n\n📂 3 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep10": "🪽 Атака титанов\n\n📂 3 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep11": "🪽 Атака титанов\n\n📂 3 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep12": "🪽 Атака титанов\n\n📂 3 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep13": "🪽 Атака титанов\n\n📂 3 Сезон — 13 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep14": "🪽 Атака титанов\n\n📂 3 Сезон — 14 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep15": "🪽 Атака титанов\n\n📂 3 Сезон — 15 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep16": "🪽 Атака титанов\n\n📂 3 Сезон — 16 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep17": "🪽 Атака титанов\n\n📂 3 Сезон — 17 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep18": "🪽 Атака титанов\n\n📂 3 Сезон — 18 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep19": "🪽 Атака титанов\n\n📂 3 Сезон — 19 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep20": "🪽 Атака титанов\n\n📂 3 Сезон — 20 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep21": "🪽 Атака титанов\n\n📂 3 Сезон — 21 Серия\n\n🔥 Приятного просмотра!",
    "titan_s3ep22": "🪽 Атака титанов\n\n📂 3 Сезон — 22 Серия\n\n🔥 Приятного просмотра!",

    "titan_s4ep1": "🪽 Атака титанов\n\n📂 4 Сезон — 1 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep2": "🪽 Атака титанов\n\n📂 4 Сезон — 2 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep3": "🪽 Атака титанов\n\n📂 4 Сезон — 3 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep4": "🪽 Атака титанов\n\n📂 4 Сезон — 4 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep5": "🪽 Атака титанов\n\n📂 4 Сезон — 5 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep6": "🪽 Атака титанов\n\n📂 4 Сезон — 6 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep7": "🪽 Атака титанов\n\n📂 4 Сезон — 7 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep8": "🪽 Атака титанов\n\n📂 4 Сезон — 8 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep9": "🪽 Атака титанов\n\n📂 4 Сезон — 9 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep10": "🪽 Атака титанов\n\n📂 4 Сезон — 10 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep11": "🪽 Атака титанов\n\n📂 4 Сезон — 11 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep12": "🪽 Атака титанов\n\n📂 4 Сезон — 12 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep13": "🪽 Атака титанов\n\n📂 4 Сезон — 13 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep14": "🪽 Атака титанов\n\n📂 4 Сезон — 14 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep15": "🪽 Атака титанов\n\n📂 4 Сезон — 15 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep16": "🪽 Атака титанов\n\n📂 4 Сезон — 16 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep17": "🪽 Атака титанов\n\n📂 4 Сезон — 17 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep18": "🪽 Атака титанов\n\n📂 4 Сезон — 18 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep19": "🪽 Атака титанов\n\n📂 4 Сезон — 19 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep20": "🪽 Атака титанов\n\n📂 4 Сезон — 20 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep21": "🪽 Атака титанов\n\n📂 4 Сезон — 21 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep22": "🪽 Атака титанов\n\n📂 4 Сезон — 22 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep23": "🪽 Атака титанов\n\n📂 4 Сезон — 23 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep24": "🪽 Атака титанов\n\n📂 4 Сезон — 24 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep25": "🪽 Атака титанов\n\n📂 4 Сезон — 25 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep26": "🪽 Атака титанов\n\n📂 4 Сезон — 26 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep27": "🪽 Атака титанов\n\n📂 4 Сезон — 27 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep28": "🪽 Атака титанов\n\n📂 4 Сезон — 28 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep29": "🪽 Атака титанов\n\n📂 4 Сезон — 29 Серия\n\n🔥 Приятного просмотра!",
    "titan_s4ep30": "🪽 Атака титанов\n\n📂 4 Сезон — 30 Серия\n\n🔥 Приятного просмотра!",
}

async def titan_menu(query, context):

    if query.data == "titan":

            await query.message.delete()

            await context.bot.send_photo(
        chat_id=query.message.chat_id,
        photo=SEASON_PHOTOS["titan_main"],
        caption="📂 Выбор сезон",
        reply_markup=InlineKeyboardMarkup(
            season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
        )
    )

    elif query.data == "titan_season1":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["titan_s1"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season1_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="titan_back")]]
            )
        )

    elif query.data == "titan_season2":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["titan_s2"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season2_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="titan_back")]]
            )
        )

    elif query.data == "titan_season3":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["titan_s3"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season3_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="titan_back")]]
            )
        )

    elif query.data == "titan_season4":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["titan_s4"],
            caption="🎬 Выбор серия",
            reply_markup=InlineKeyboardMarkup(
                season4_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="titan_back")]]
            )
        )

    elif query.data == "titan_back":

        await query.message.delete()

        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=SEASON_PHOTOS["titan_main"],
            caption="📂 Выбор сезон",
            reply_markup=InlineKeyboardMarkup(
                season_buttons + [[InlineKeyboardButton("❌ Закрыть", callback_data="back_catalog")]]
            )
        )

    elif query.data == "titan_close":

        await query.message.delete()

    elif query.data == "titan_close_series":

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
                [InlineKeyboardButton("❌ Закрыть", callback_data="titan_close_series")]
            ])
        )

>>>>>>> 0ce684e35d73729033b4f65cf6c877d8cb663463
        context.user_data["video_msg"] = msg.message_id