import asyncio
import logging
import sys


from create_bot import bot, dp
from handlers.other import register_handlers_other


async def main() -> None:
    register_handlers_other(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def on_startup():
    print('Бот Запущен')


async def on_shutdown():
    print('Бот остановлен')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
