import asyncio

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tg_bot import config
from tg_bot.loader import dp, bot
from aiogram.filters import Command
from tg_bot.admin.kb import admin_kb
from tg_bot.user.kb import user_kb

# запкускаем кнопку web_app сбоку от поля ввода
async def set_web_app_button():
    await bot.set_chat_menu_button(
        menu_button=types.MenuButtonWebApp(
            text="Играть",  # Текст на кнопке
            web_app=types.WebAppInfo(url='ССЫЛКА') # вставляем ссылку на веб-приложение
        )
    )

# Команда /start с проверкой ID пользователя является он админом или юзером
@dp.message(Command(commands=['start']))
async def start_command(message: types.Message):
    await set_web_app_button() # запуск кнопки
    user_id = message.from_user.id

    # проверка на админа
    if user_id in config.admins:
        await message.answer("Привет, ты находишься на странице админа", reply_markup=admin_kb)
    else:
        await message.answer("Привет, скорее запускай игру, нажав кнопку ниже!", reply_markup=user_kb)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
