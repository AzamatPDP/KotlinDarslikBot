from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menuKopiryating = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-muallif darslari"),
            KeyboardButton(text="2-muallif darslari"),
        ],
        [
            KeyboardButton(text="🔙Orqaga"),
            KeyboardButton(text="Asosiy Menyu"),
        ],

    ],
    resize_keyboard=True
)