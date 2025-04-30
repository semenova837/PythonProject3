import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiogram import Router, F
from aiogram.types import Message
import json

search_router = Router()

with open("data/database.json", encoding="utf-8") as f:
    db = json.load(f)

@search_router.message(F.text == "🔍 Пошук")
async def search_intro(message: Message):
    await message.answer("🔍 Надішліть назву книги або пісні, яку хочете знайти:")

@search_router.message()
async def handle_search(message: Message):
    ignored_phrases = [
        "📚", "🎵", "🔠", "👩‍🏫", "📅", "🗂️", "Жанр", "🔍", "✨", "ℹ️", "Головне меню"
    ]
    if any(p in message.text for p in ignored_phrases):
        return

    query = message.text.lower()
    found_books = [b for b in db["books"] if query in b["title"].lower()]
    found_music = [m for m in db["music"] if query in m["title"].lower()]

    response = ""
    if found_books:
        response += "📚 Знайдено книги:\n" + "\n".join(
            [f'{b["title"]} — {b["author"]} ({b["year"]})' for b in found_books])
    if found_music:
        if response:
            response += "\n\n"
        response += "🎧 Знайдено пісні:\n" + "\n".join(
            [f'{m["title"]} — {m["artist"]} ({m["year"]})' for m in found_music])

    if not response:
        response = "😔 Нічого не знайдено за вашим запитом."

    await message.answer(response)
