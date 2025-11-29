from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Создать смену")]],
        resize_keyboard=True
    )
