from aiogram import html, Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message

from States import Form


async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


def register_handlers_other(router: Router) -> None:
    router.message.register(command_start_handler, CommandStart())
    router.message.register(echo_handler)
