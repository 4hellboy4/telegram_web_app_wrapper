from aiogram import types, Router

user = Router()

@user.message(lambda message: message.text == "Играть")
async def order_food(message: types.Message):
    await message.reply("Хорошeй вам игры!")