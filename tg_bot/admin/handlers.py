from aiogram import types, Router
from tg_bot import config

admin = Router()

@admin.message(lambda message: message.text == "Протестировать" and message.from_user.id in config.admins)
async def manage_orders(message: types.Message):
    await message.reply("Вы открыли админ приложение")