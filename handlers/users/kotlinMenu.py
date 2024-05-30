from aiogram.types import Message

from keyboards.default.dasturlash import menuLanguage
from keyboards.default.kotlinKeyboard import menuKotlin
from keyboards.default.startKeyboard import menuStart

from loader import dp

@dp.message_handler(text="Kotlin")
async def send_link(message: Message):
    await message.answer("Mentor: Zohidjon Akbarov\n"
                         "Mavzuni tanlang", reply_markup=menuKotlin)

@dp.message_handler(text="#01-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=NsydPMykpUk&list=PLuPg3DDVpiJdOEXwgsloQbLg8RHYBnivr&index=1&pp=iAQB")

@dp.message_handler(text="#02-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=qlTVOhW3Hss&list=PLuPg3DDVpiJdOEXwgsloQbLg8RHYBnivr&index=2&pp=iAQB")

@dp.message_handler(text="#03-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=df6aiTgQ0-U&list=PLuPg3DDVpiJdOEXwgsloQbLg8RHYBnivr&index=3&pp=iAQB")

@dp.message_handler(text="#04-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=FmKU_kA3bAw&list=PLuPg3DDVpiJdOEXwgsloQbLg8RHYBnivr&index=4&pp=iAQB")

@dp.message_handler(text="#05-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=qvvUpMjy4GA&list=PLuPg3DDVpiJdOEXwgsloQbLg8RHYBnivr&index=5&pp=iAQB")

@dp.message_handler(text="#06-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=VSmafGIas88&list=PLuPg3DDVpiJdOEXwgsloQbLg8RHYBnivr&index=6&pp=iAQB")

@dp.message_handler(text="#07-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=mosTZL54WFs&list=PLuPg3DDVpiJdOEXwgsloQbLg8RHYBnivr&index=7&pp=iAQB")

@dp.message_handler(text="#08-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=kVaFMevJ4TY&list=PLuPg3DDVpiJdOEXwgsloQbLg8RHYBnivr&index=8&pp=iAQB")

@dp.message_handler(text="#09-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=-9jQOE_H-rs&list=PLuPg3DDVpiJdOEXwgsloQbLg8RHYBnivr&index=9&pp=iAQB")

@dp.message_handler(text="#10-dars")
async def send_link(message: Message):
    await message.answer("https://www.youtube.com/watch?v=_rNNiIyqjV0&list=PLuPg3DDVpiJdOEXwgsloQbLg8RHYBnivr&index=10&pp=iAQB")

@dp.message_handler(text="Asosiy Menyu")
async def send_link(message: Message):
    await message.answer("Kursni tanlang", reply_markup=menuStart)

@dp.message_handler(text="🔙Ortga")
async def send_link(message: Message):
    await message.answer("Dasturlash tilini tanlang", reply_markup=menuLanguage)