from aiogram import types, Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from create_bot import bot
from questionnaire.states.state import Form


async def no_sticker_test(message: types.Message) -> None:
    await message.answer("Во время теста не спамь стикерами")


async def one_question(message: types.Message, state: FSMContext) -> None:
    await bot.send_message(chat_id=message.chat.id, text="Это был первый вопрос")
    await state.set_state(Form.one)


async def two_question(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['first_message'] = message.text
    await state.update_data(data)
    await bot.send_message(chat_id=message.chat.id, text="Это был второй вопрос")
    await state.set_state(Form.two)


async def three_question(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['second_message'] = message.text
    await state.update_data(data)
    await bot.send_message(chat_id=message.chat.id, text="Это был третий вопрос")
    await state.set_state(Form.three)


async def after_question(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    data['third_message'] = message.text
    first_message = data['first_message']
    second_message = data['second_message']
    third_message = data['third_message']
    text_message = f"А вот что ты мне понаписал!\n" \
                   f"Первое сообщение: {first_message}\n" \
                   f"Второе сообщение: {second_message}\n" \
                   f"Третье сообщение: {third_message}\n"
    await bot.send_message(
        chat_id=message.chat.id,
        text=text_message)
    await state.clear()


def register_questionnaire(router: Router) -> None:
    router.message.register(no_sticker_test, F.content_type.in_({'sticker', 'photo'}), StateFilter(Form))
    router.message.register(one_question, Command("questionnaire"), StateFilter(None))
    router.message.register(two_question, F.text, StateFilter(Form.one))
    router.message.register(three_question, F.text, StateFilter(Form.two))
    router.message.register(after_question, F.text, StateFilter(Form.three))
