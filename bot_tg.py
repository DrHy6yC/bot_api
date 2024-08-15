import asyncio
import logging
import sys


from create_bot import bot, dp
from other import register_handlers_other
from inline_mode.handlers.inline import register_inline_handler
from questionnaire.handler import register_questionnaire


async def main() -> None:
    register_inline_handler(dp)
    register_questionnaire(dp)
    register_handlers_other(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def on_startup():
    print('Бот Запущен')


async def on_shutdown():
    print('Бот остановлен')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
    # except Exception as exeption:
    #     print(f"Бот упал c ошибкой:\n{exeption}")
