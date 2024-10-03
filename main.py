import asyncio
from email import message_from_string

from aiogram import types
from aiogram.utils.deep_linking import create_start_link, decode_payload
from tg_bot import config
from tg_bot.loader import dp, bot
from aiogram.filters import CommandStart
from aiogram.filters import Command
from tg_bot.admin.kb import admin_kb
from tg_bot.user.kb import user_kb

# Запускаем кнопку web_app сбоку от поля ввода
async def set_web_app_button():
    await bot.set_chat_menu_button(
        menu_button=types.MenuButtonWebApp(
            text="Играть",  # Текст на кнопке
            web_app=types.WebAppInfo(url='ССЫЛКА')  # Вставляем ссылку на веб-приложение
        )
    )

# Генерация deeplink с параметром startapp
async def generate_deeplink(user_id):
    # Генерация ссылки с переданным user_id в качестве параметра
    link = await create_start_link(bot, f'start={user_id}', encode=True)  # Используем start=
    return link

# Обработка команды /start с deep linking
@dp.message(Command(commands=['start']))
async def start_command(message: types.Message):
    await set_web_app_button()  # запуск кнопки

    url_code = await generate_deeplink(message.from_user.id)

    # Извлекаем аргументы после команды /start
    start_param = message.text.split(' ')[1] if len(message.text.split(' ')) > 1 else None

    await message.answer(f'Привет, ваша генеральная ссылка - {url_code}')

    user_id = message.from_user.id
    # Проверка на админа
    if user_id in config.admins:
        await message.answer("Привет, ты находишься на странице админа", reply_markup=admin_kb)
    else:
        if start_param:
            # Декодируем параметр (если он закодирован base64)
            referrer_id = decode_payload(start_param)
            await message.answer(f"Вас пригласил пользователь с ID {referrer_id}", reply_markup=user_kb)
        else:
            await message.answer("Привет! Запускайте игру, нажав кнопку ниже!", reply_markup=user_kb)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
