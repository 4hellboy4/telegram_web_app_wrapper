from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

user_kb_builder = InlineKeyboardBuilder()
user_kb_builder.button(text="Играть", callback_data="Играть", web_app=types.WebAppInfo(url='ССЫЛКА'))
user_kb = user_kb_builder.as_markup(resize_keyboard=True)