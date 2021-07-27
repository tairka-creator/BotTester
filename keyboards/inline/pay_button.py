from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# from keyboards.inline.callback_data import callback_pay, callback_check

button_pay = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подписка", callback_data="подписка"),
            # InlineKeyboardButton(text="Проверить подписку", callback_data="Проверить подписку"),
        ]
    ]
)

button_pay_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text='Назад', callback_data="back_pay")
        ]
    ]
)