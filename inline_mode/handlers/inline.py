import hashlib
from aiogram import types, Router
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

from bot_main.utils.translator import translate_text
from bot_main.utils.text_function import detect_en_symbol


async def inline_translate(inline_query: types.InlineQuery) -> None:
    print('start inline')
    text_inline_query = inline_query.query or 'Введи то что хочешь перевести'
    en_ru = detect_en_symbol(text_inline_query)
    translated_text = translate_text(text_inline_query, en_ru)
    input_text = f'{text_inline_query} -> {translated_text}'
    input_text_message = InputTextMessageContent(message_text=input_text)
    result_id = hashlib.md5(translated_text.encode()).hexdigest()
    item = InlineQueryResultArticle(
        input_message_content=input_text_message,
        id=result_id,
        title=str(translated_text)
    )
    print(result_id)
    await inline_query.answer(results=[item], cache_time=5, is_personal=True)


def register_inline_handler(router: Router) -> None:
    router.inline_query.register(inline_translate)
