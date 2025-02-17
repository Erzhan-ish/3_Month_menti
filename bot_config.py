from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values

from database import Database

token = dotenv_values('.env')['BOT_TOKEN']
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=storage)
database = Database('database.sqlite')
