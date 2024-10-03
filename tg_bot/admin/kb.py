from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

admin_kb_builder = InlineKeyboardBuilder()
admin_kb_builder.button(text="Протестировать", callback_data="Протестировать", web_app=types.WebAppInfo(url='ССЫЛКА'))
admin_kb = admin_kb_builder.as_markup(resize_keyboard=True)