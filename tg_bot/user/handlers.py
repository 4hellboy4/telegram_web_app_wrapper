from aiogram import types, Router

user = Router() # отдельный роут для пользователей

@user.callback_query(lambda callback_query: callback_query.data == "Играть")
async def order_food(callback_query: types.CallbackQuery):
    await callback_query.message.reply("Хорошeй вам игры!")