from aiogram.types import Message
from keyboards.default.kopiryatingKeyboard import menuKopiryating
from keyboards.default.startKeyboard import menuStart

from loader import dp

@dp.message_handler(text="📝Kopiryating")
async def send_link(message: Message):
    await message.answer("Darslarni tanlang", reply_markup=menuKopiryating)


@dp.message_handler(text="🔙Ortga")
async def send_link(message: Message):
    await message.answer("Darslarni tanlang!", reply_markup=menuKopiryating)

@dp.message_handler(text="🔙Orqaga")
async def send_link(message: Message):
    await message.answer("Kursni tanlang!", reply_markup=menuStart)


@dp.message_handler(text="Asosiy Menyu")
async def send_link(message: Message):
    await message.answer("Kursni tanlang!", reply_markup=menuStart)

