from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menuLanguage = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kotlin'),
            KeyboardButton(text='Python'),
            KeyboardButton(text='C++'),
        ],
        [
            KeyboardButton(text="🔙Orqaga"),
            KeyboardButton(text="Asosiy Menyu"),
        ],

    ],
    resize_keyboard=True
)