from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

recommendations_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📖 Книжкові поради")], [KeyboardButton(text="🎧 Музичні поради")], [KeyboardButton(text="🔙 Головне меню")]],
    resize_keyboard=True
)