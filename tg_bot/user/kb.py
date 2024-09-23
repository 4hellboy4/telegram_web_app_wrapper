from aiogram.utils.keyboard import ReplyKeyboardBuilder

user_kb_builder = ReplyKeyboardBuilder()
user_kb_builder.button(text="Играть", web_app="ССЫЛКА")
user_kb = user_kb_builder.as_markup(resize_keyboard=True)