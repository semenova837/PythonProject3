import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from config import TOKEN
from keyboards.main_menu import main_menu_kb

from handlers.books import books_router
from handlers.music import music_router
from handlers.search import search_router

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_router(books_router)
dp.include_router(music_router)
dp.include_router(search_router)

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer(
        "👋 Привіт! Я бот для ознайомлення з українською культурою: літературою та музикою.\n"
        "Оберіть дію з меню нижче:",
        reply_markup=main_menu_kb
    )

@dp.message(F.text == "🔙 Головне меню")
async def return_to_main_menu(message: Message):
    await message.answer("🏠 Ви повернулися до головного меню:", reply_markup=main_menu_kb)

@dp.message(F.text == "✨ Рекомендації")
async def show_recommendations(message: Message):
    await message.answer(
        """📚 Рекомендовані книги та треки:
        
1. «Фелікс Австрія» — Софія Андрухович + «Обійми» — Океан Ельзи
            
2. «Записки українського самашедшого» — Ліна Костенко + «Плакала» — KAZKA
            
3. «Тіні забутих предків» — Михайло Коцюбинський + «Додому» — ONUKA
            
📖📻 Гармонійні поєднання для натхнення 💫"""
    )

@dp.message(F.text == "ℹ️ Про бота")
async def about_bot(message: Message):
    await message.answer(
        """🤖 <b>Про бота</b>:

• Створено для ознайомлення з українською музикою та літературою
• Функції: сортування, пошук, рекомендації
• Розробник: Семенова Дар'я 
            
Зроблено з любовʼю до української культури 🇺🇦"""
    )

if __name__ == "__main__":
    print("✅ Ukrainian Culture Bot запущено.")
    asyncio.run(dp.run_polling(bot))
