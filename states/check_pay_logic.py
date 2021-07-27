from aiogram.dispatcher.filters.state import StatesGroup, State


class Check_pay_logic(StatesGroup):
    MessagePay = State()


class Go_To_Bot(StatesGroup):
    bot_start = State()
