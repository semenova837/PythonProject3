import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from states import SortStates
import json

with open("data/database.json", encoding="utf-8") as f:
    db = json.load(f)

music_router = Router()

@music_router.message(F.text == "🎵 Музика")
async def show_music_menu(message: Message, state: FSMContext):
    from keyboards.music_menu import music_menu_kb
    await state.set_state(SortStates.ChoosingCategory)
    await state.update_data(category="music")
    await message.answer("🎵 Оберіть спосіб сортування музики:", reply_markup=music_menu_kb)

@music_router.message(F.text == "🎧 Сортувати за назвою")
async def sort_music_by_title(message: Message):
    sorted_music = sorted(db["music"], key=lambda x: x["title"])
    text = "\n\n".join([f'<b>{m["title"]}</b> — {m["artist"]} ({m["year"]})' for m in sorted_music[:10]])
    await message.answer("🔠 Топ 10 пісень за назвою:\n" + text)

@music_router.message(F.text == "🎤 Сортувати за виконавцем")
async def sort_music_by_artist(message: Message):
    sorted_music = sorted(db["music"], key=lambda x: x["artist"])
    text = "\n\n".join([f'<b>{m["title"]}</b> — {m["artist"]} ({m["year"]})' for m in sorted_music[:10]])
    await message.answer("🎤 Топ 10 треків за виконавцем:\n" + text)

@music_router.message(F.text == "🎧 Сортувати за роком")
async def sort_music_by_year(message: Message):
    sorted_music = sorted(db["music"], key=lambda x: x["year"])
    text = "\n\n".join([f'<b>{m["title"]}</b> — {m["artist"]} ({m["year"]})' for m in sorted_music[:10]])
    await message.answer("📅 Топ 10 пісень за роком:\n" + text)

@music_router.message(F.text == "🎧 Сортувати за жанром")
async def sort_music_by_genre(message: Message, state: FSMContext):
    await state.set_state(SortStates.ChoosingGenre)
    await state.update_data(category="music")
    genres = sorted(set(m["genre"] for m in db["music"]))
    genre_buttons = [[KeyboardButton(text=f"🎧 Жанр: {g}")] for g in genres]
    genre_kb = ReplyKeyboardMarkup(keyboard=genre_buttons + [[KeyboardButton(text="🔙 Головне меню")]], resize_keyboard=True)
    await message.answer("🗂️ Оберіть жанр:", reply_markup=genre_kb)

@music_router.message(F.text.startswith("🎧 Жанр: "))
async def show_music_by_genre(message: Message, state: FSMContext):
    genre = message.text.replace("🎧 Жанр: ", "")
    filtered = [m for m in db["music"] if m["genre"] == genre][:10]
    text = "".join([f'<b>{m["title"]}</b> — {m["artist"]} ({m["year"]})' for m in filtered])
    await message.answer(f"🎧 Треки у жанрі <b>{genre}</b>:{text}")