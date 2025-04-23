from aiogram.fsm.state import StatesGroup, State

class SortStates(StatesGroup):
    ChoosingCategory = State()
    ChoosingGenre = State()