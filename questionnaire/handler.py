from aiogram import types, Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from create_bot import bot


class Form(StatesGroup):
    one = State()
    two = State()
    three = State()


async def one_question(message: types.Message, state: FSMContext) -> None:
    await bot.send_message(chat_id=message.chat.id, text="Это был первый вопрос")
    await state.set_state(Form.one)


async def two_question(message: types.Message, state: FSMContext) -> None:
    await bot.send_message(chat_id=message.chat.id, text="Это был второй вопрос")
    await state.set_state(Form.two)


async def three_question(message: types.Message, state: FSMContext) -> None:
    await bot.send_message(chat_id=message.chat.id, text="Это был третий вопрос")
    await state.set_state(Form.three)


async def after_question(message: types.Message, state: FSMContext) -> None:
    await bot.send_message(chat_id=message.chat.id, text="А вот что ты мне понаписал!")
    await state.clear()


def register_questionnaire(router: Router) -> None:
    router.message.register(one_question, CommandStart(), StateFilter(None))
    router.message.register(two_question, F.text, StateFilter(Form.one))
    router.message.register(three_question, F.text, StateFilter(Form.two))
    router.message.register(after_question, F.text, StateFilter(Form.three))
