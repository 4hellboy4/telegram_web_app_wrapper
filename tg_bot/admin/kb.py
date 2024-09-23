from aiogram.utils.keyboard import InlineKeyboardBuilder

admin_kb_builder = InlineKeyboardBuilder()
admin_kb_builder.button(text="Протестировать", callback_data="Протестировать", web_app="ССЫЛКА")
admin_kb = admin_kb_builder.as_markup(resize_keyboard=True)