from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Книги"), KeyboardButton(text="🎵 Музика")],
        [KeyboardButton(text="🔍 Пошук"), KeyboardButton(text="✨ Рекомендації")],
        [KeyboardButton(text="ℹ️ Про бота")]
    ],
    resize_keyboard=True
)