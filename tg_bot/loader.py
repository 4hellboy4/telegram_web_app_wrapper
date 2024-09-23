from aiogram import Bot, Dispatcher

from tg_bot.config import BOT_TOKEN
from tg_bot.admin.handlers import admin
from tg_bot.user.handlers import user

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(admin)
dp.include_router(user)
