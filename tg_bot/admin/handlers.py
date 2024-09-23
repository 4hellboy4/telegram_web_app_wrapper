from aiogram import types, Router

from tg_bot import config

admin = Router() # создаем отдельный роут для админа

@admin.callback_query(lambda callback_query: callback_query.data == "Протестировать" and callback_query.from_user.id in config.admins)
async def manage_orders(callback_query: types.CallbackQuery):
    await callback_query.message.reply("Вы открыли админ приложение")