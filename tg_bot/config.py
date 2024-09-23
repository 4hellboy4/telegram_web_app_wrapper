import os

from dotenv import load_dotenv

load_dotenv() # достаем переменные из .env.example

BOT_TOKEN = os.getenv('BOT_TOKEN')

admins: list[int] = [367757357] # все id админов
