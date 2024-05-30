from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuKotlin = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="#01-dars"),
            KeyboardButton(text="#02-dars"),
            KeyboardButton(text="#03-dars"),
        ],
[
            KeyboardButton(text="#04-dars"),
            KeyboardButton(text="#05-dars"),
            KeyboardButton(text="#06-dars"),
        ],
[
            KeyboardButton(text="#07-dars"),
            KeyboardButton(text="#08-dars"),
            KeyboardButton(text="#09-dars"),
        ],
[
            KeyboardButton(text="#10-dars"),
        ],
        [
            KeyboardButton(text="🔙Ortga"),
            KeyboardButton(text="Asosiy Menyu"),
        ],
    ],
    resize_keyboard=True
)

