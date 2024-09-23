import asyncio

from aiogram import types

from tg_bot import config
from tg_bot.loader import dp, bot
from aiogram.filters import Command
from tg_bot.admin.kb import admin_kb
from tg_bot.user.kb import user_kb

# Команда /start с проверкой ID пользователя
@dp.message(Command(commands=['start']))
async def start_command(message: types.Message):
    user_id = message.from_user.id

    if user_id in config.admins:
        # Ответ для админа
        await message.answer("Привет, ты находишься на странице админа", reply_markup=admin_kb)
    else:
        # Ответ для обычного пользователя
        await message.answer("Привет, ты можешь запустить приложение, нажав на кнопку снизу", reply_markup=user_kb)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
