from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_Button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="О нас"),
            KeyboardButton(text="Создать инвест портфель")
        ]
    ],
    resize_keyboard=True
)