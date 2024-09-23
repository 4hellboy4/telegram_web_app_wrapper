from aiogram.utils.keyboard import ReplyKeyboardBuilder

admin_kb_builder = ReplyKeyboardBuilder()
admin_kb_builder.button(text="Протестировать", web_app="ССЫЛКА")
admin_kb = admin_kb_builder.as_markup(resize_keyboard=True)