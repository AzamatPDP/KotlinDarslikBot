from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menuMobilograf = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-bo'lim"),
            KeyboardButton(text="2-bo'lim"),
        ],
        [
            KeyboardButton(text="🔙Orqaga"),
            KeyboardButton(text="Asosiy Menyu"),
        ],

    ],
    resize_keyboard=True
)