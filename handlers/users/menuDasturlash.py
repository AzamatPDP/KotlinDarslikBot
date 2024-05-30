from aiogram.types import Message
from keyboards.default.dasturlash import menuLanguage
from keyboards.default.startKeyboard import menuStart

from loader import dp

@dp.message_handler(text="💻Dasturlash")
async def send_link(message: Message):
    await message.answer("Dasturlash tilini tanlang", reply_markup=menuLanguage)


@dp.message_handler(text="🔙Ortga")
async def send_link(message: Message):
    await message.answer("Dasturlash tilini tanlang!", reply_markup=menuLanguage)

@dp.message_handler(text="🔙Orqaga")
async def send_link(message: Message):
    await message.answer("Kursni tanlang!", reply_markup=menuStart)


@dp.message_handler(text="Asosiy Menyu")
async def send_link(message: Message):
    await message.answer("Kursni tanlang!", reply_markup=menuStart)

