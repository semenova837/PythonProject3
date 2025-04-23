from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

search_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🔍 Пошук за назвою")], [KeyboardButton(text="🔙 Головне меню")]],
    resize_keyboard=True
)