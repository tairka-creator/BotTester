from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def buy_keyboard(item_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardMarkup(text='Оплатить', callback_data="buy")
            ],
            [
                InlineKeyboardMarkup(text='Назад', callback_data="back_pay")
            ]
        ]
    )
    return keyboard


paid_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Проверить оплату", callback_data="paid")
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ],
    ]
)

go_to_bot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Перейти к боту", callback_data="main_button_one")
        ]
    ]
)