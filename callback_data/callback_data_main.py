from aiogram.filters.callback_data import CallbackData


class DelMessageCal(CallbackData, prefix='del_message'):
    pass


del_message = DelMessageCal()
