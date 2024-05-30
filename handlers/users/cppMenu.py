from aiogram.types import Message
from keyboards.default.cppKeyboard import menuCpp
from keyboards.default.dasturlash import menuLanguage
from keyboards.default.startKeyboard import menuStart

from loader import dp
@dp.message_handler(text="C++")
async def send_link(message: Message):
    await message.answer("Darsni tanlang", reply_markup=menuCpp)

@dp.message_handler(text="#1-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=2BlETkdYFJk&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo&index=1&pp=iAQB")

@dp.message_handler(text="#2-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=pYiGITH2z3s&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo&index=2&pp=iAQB")

@dp.message_handler(text="#3-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=IgO3wN-17yw&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo&index=3&pp=iAQB")

@dp.message_handler(text="#4-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=rUyAdWKZTKU&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo&index=4&pp=iAQB")

@dp.message_handler(text="#5-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=6uLHsaXxTNE&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo&index=5&pp=iAQB")

@dp.message_handler(text="#6-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=mPVGvWQkCNg&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo&index=6&pp=iAQB")

@dp.message_handler(text="#7-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=ufc4Skq9yPQ&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo&index=7&pp=iAQB")

@dp.message_handler(text="#8-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=3JeOu6xCXXw&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo&index=8&pp=iAQB")

@dp.message_handler(text="#9-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=1fEOxCwBymI&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo&index=9&pp=iAQB")

@dp.message_handler(text="#10-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=BMCQQn93cF4&list=PLY4N-4FJdZQCzjRxjFfHQ57xAYvKmk2Yo&index=10&pp=iAQB")

@dp.message_handler(text="Asosiy Menyu")
async def send_link(message: Message):
    await message.answer("Kursni tanlang", reply_markup=menuStart)

@dp.message_handler(text="🔙Ortga")
async def send_link(message: Message):
    await message.answer("Dasturlash tilini tanlang", reply_markup=menuLanguage)