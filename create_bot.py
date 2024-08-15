from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from config import TOKEN, REDIS, REDIS_HOST, REDIS_PORT


redis_url = f"{REDIS}://{REDIS_HOST}:{REDIS_PORT}"

storage = RedisStorage.from_url(redis_url)
dp = Dispatcher(storage=storage)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
