from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


button_3_question = InlineKeyboardMarkup(
    inline_keyboard=[
        # [
        #     InlineKeyboardButton(text="Паттерны уже работают", callback_data="patterns_working")
        # ],
        # [
        #     InlineKeyboardButton(text="Планируемые сделки", callback_data="planned_transactions")
        # ],
        [
            InlineKeyboardButton(text="Назад", callback_data="Up_to_12_months")
        ]
    ]
)