from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

load_dotenv()
TOKEN = getenv("BOT_TOKEN")


storage = RedisStorage.from_url("redis://localhost:6380")
dp = Dispatcher(storage=storage)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
