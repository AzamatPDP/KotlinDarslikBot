from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💻Dasturlash'),
            KeyboardButton(text='📲Mobilografiya'),
        ],
        [
            KeyboardButton(text='📝Kopiryating'),
        ],
    ],
    resize_keyboard=True
)