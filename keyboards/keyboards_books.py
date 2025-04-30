from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

books_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔠 Сортувати за назвою")],
        [KeyboardButton(text="👩‍🏫 Сортувати за автором")],
        [KeyboardButton(text="🗂️ Сортувати за жанром")],
        [KeyboardButton(text="📅 Сортувати за роком")],
        [KeyboardButton(text="🔙 Головне меню")]
    ],
    resize_keyboard=True
)
