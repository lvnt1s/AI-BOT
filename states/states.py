from aiogram.fsm.state import State, StatesGroup

class deposit(StatesGroup):
    amount = State()
    payment_method = State()


