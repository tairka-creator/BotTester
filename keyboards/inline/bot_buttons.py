from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# from keyboards.inline.callback_data import callback_pay, callback_check

button_1_logic = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Составить инвест портфель", callback_data="create_bag"),
        ],
        [
            InlineKeyboardButton(text="О нас", callback_data="about_us"),
        ]
    ]
)

button_2_logic_about_us = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Правила по сделкам", callback_data="Rules_for_transactions")
        ],
        [
            InlineKeyboardButton(text="Информация по рынку", callback_data="Market_information")
        ],
        [
            InlineKeyboardButton(text="Общая информация", callback_data="General_information")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="main_button_one")
        ]
    ]
)

button_2_logic_create_bag_q1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="До 12 месяцев", callback_data="Up_to_12_months"),
            InlineKeyboardButton(text="От 3 лет", callback_data="From_3_years_old")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="main_button_one")
        ]
    ]
)

bitton_3_logoc_back_about_us = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="about_us")
        ]
    ]
)

bitton_3_logoc_back_create_bag = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Паттерны уже работают", callback_data="patterns_working")
        ],
        [
            InlineKeyboardButton(text="Планируемые сделки", callback_data="planned_transactions")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="create_bag")
        ]
    ]
)

# Для логики инвестирования от 3 лет переделать
bitton_3_logoc_back_create_bag_test = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data="create_bag")
        ]
    ]
)