from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

books_sort_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="За жанром", callback_data="sort_books_genre")],
    [InlineKeyboardButton(text="За автором", callback_data="sort_books_author")],
    [InlineKeyboardButton(text="За роком", callback_data="sort_books_year")]
])

music_sort_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="За жанром", callback_data="sort_music_genre")],
    [InlineKeyboardButton(text="За виконавцем", callback_data="sort_music_artist")],
    [InlineKeyboardButton(text="За роком", callback_data="sort_music_year")],
    [InlineKeyboardButton(text="За країною", callback_data="sort_music_country")]
])
