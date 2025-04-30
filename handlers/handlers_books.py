import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from states.states import SortStates
import json

with open("data/database.json", encoding="utf-8") as f:
    db = json.load(f)

books_router = Router()

@books_router.message(F.text == "📚 Книги")
async def show_books_menu(message: Message, state: FSMContext):
    from keyboards.keyboards_books import books_menu_kb
    await state.set_state(SortStates.ChoosingCategory)
    await state.update_data(category="books")
    await message.answer("📚 Оберіть спосіб сортування книг:", reply_markup=books_menu_kb)

@books_router.message(F.text == "🔠 Сортувати за назвою")
async def sort_books_by_title(message: Message):
    sorted_books = sorted(db["books"], key=lambda x: x["title"])
    text = "\n\n".join([f'<b>{b["title"]}</b> — {b["author"]} ({b["year"]})' for b in sorted_books[:10]])
    await message.answer("🔠 Топ 10 книг за назвою:\n" + text)

@books_router.message(F.text == "👩‍🏫 Сортувати за автором")
async def sort_books_by_author(message: Message):
    sorted_books = sorted(db["books"], key=lambda x: x["author"])
    text = "\n\n".join([f'<b>{b["title"]}</b> — {b["author"]} ({b["year"]})' for b in sorted_books[:10]])
    await message.answer("👩‍🏫 Топ 10 книг за автором:\n" + text)

@books_router.message(F.text == "📅 Сортувати за роком")
async def sort_books_by_year(message: Message):
    sorted_books = sorted(db["books"], key=lambda x: x["year"])
    text = "\n\n".join([f'<b>{b["title"]}</b> — {b["author"]} ({b["year"]})' for b in sorted_books[:10]])
    await message.answer("📅 Топ 10 книг за роком:\n" + text)

@books_router.message(F.text == "🗂️ Сортувати за жанром")
async def sort_books_by_genre(message: Message, state: FSMContext):
    await state.set_state(SortStates.ChoosingGenre)
    await state.update_data(category="books")
    genres = sorted(set(book["genre"] for book in db["books"]))
    genre_buttons = [[KeyboardButton(text=f"📚 Жанр: {g}")] for g in genres]
    genre_kb = ReplyKeyboardMarkup(keyboard=genre_buttons + [[KeyboardButton(text="🔙 Головне меню")]], resize_keyboard=True)
    await message.answer("🗂️ Оберіть жанр:", reply_markup=genre_kb)

@books_router.message(F.text.startswith("📚 Жанр: "))
async def show_books_by_genre(message: Message, state: FSMContext):
    genre = message.text.replace("📚 Жанр: ", "")
    filtered = [b for b in db["books"] if b["genre"] == genre][:10]

    if not filtered:
        await message.answer("❌ Немає книг у цьому жанрі.")
        return

    for book in filtered:
        caption = (
            f"<b>{book['title']}</b>\n"
            f"✍️ {book['author']} ({book.get('year', 'рік невідомий')})\n"
        )

        if "image" in book and book["image"]:
            await message.answer_photo(photo=book["image"], caption=caption, parse_mode="HTML")
        else:
            await message.answer(caption, parse_mode="HTML")
