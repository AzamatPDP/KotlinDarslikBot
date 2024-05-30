from aiogram.types import Message
from keyboards.default.pythonKeyboard import menuPython
from keyboards.default.dasturlash import menuLanguage
from keyboards.default.startKeyboard import menuStart

from loader import dp

@dp.message_handler(text="Python")
async def send_link(message: Message):
    await message.answer("Mavzuni tanlang", reply_markup=menuPython)

@dp.message_handler(text="1-dars")
async def send_link(message: Message):
    await message.answer("Kirish: https://www.youtube.com/watch?v=nitlLnbp7ak&t=225s")

@dp.message_handler(text="2-dars")
async def send_link(message: Message):
    await message.answer("Birinchi dasturimiz: https://www.youtube.com/watch?v=dguiNk8eHPY ")

@dp.message_handler(text="4-dars")
async def send_link(message: Message):
    await message.answer("O'zgaruvchilar:https://www.youtube.com/watch?v=4-Sj_owtx3Q ")

@dp.message_handler(text="3-dars")
async def send_link(message: Message):
    await message.answer("Arifmetik amallar bilan ishlash: https://www.youtube.com/watch?v=djtv5NMIBSY ")

@dp.message_handler(text="5-dars")
async def send_link(message: Message):
    await message.answer("Matn bilan ishlash: https://www.youtube.com/watch?v=ne2ZoZ7q3UY ")

@dp.message_handler(text="6-dars")
async def send_link(message: Message):
    await message.answer("Sonlar bilan ishlash: https://www.youtube.com/watch?v=_1eGzQpAtC8  ")

@dp.message_handler(text="7-dars")
async def send_link(message: Message):
    await message.answer("Lists(ro'yxatlar): https://www.youtube.com/watch?v=92UuA1jneuQ ")

@dp.message_handler(text="8-dars")
async def send_link(message: Message):
    await message.answer("Ro'yxatlar bilan ishlash: https://www.youtube.com/watch?v=019Dzhf0rB0 ")

@dp.message_handler(text="9-dars")
async def send_link(message: Message):
    await message.answer("For tsikli: https://www.youtube.com/watch?v=982dbRh0Efg ")

@dp.message_handler(text="10-dars")
async def send_link(message: Message):
    await message.answer("If else shartlari va tarmoqlanish: https://www.youtube.com/watch?v=QH5Q_dyj3dI ")

@dp.message_handler(text="Asosiy Menyu")
async def send_link(message: Message):
    await message.answer("Kursni tanlang", reply_markup=menuStart)

@dp.message_handler(text="🔙Ortga")
async def send_link(message: Message):
    await message.answer("Dasturlash tilini tanlang", reply_markup=menuLanguage)