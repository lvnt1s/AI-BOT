from aiogram.utils.keyboard import ReplyKeyboardBuilder,KeyboardBuilder,ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from core.config_reader import settings

async def menu(user_id: int) -> ReplyKeyboardMarkup:
    """Создание меню для пользователя."""
    keyboard_builder = ReplyKeyboardBuilder()
    
    keyboard_builder.row(
        KeyboardButton(text="🤖 Меню")
    )
    keyboard_builder.row(
        KeyboardButton(text="📂 Профиль"),
        KeyboardButton(text="ℹ️ Информация")
    )

    if user_id == settings.ADMIN_ID:
        keyboard_builder.row(
        KeyboardButton(text="⚙️ Админ-панель")
    )
    
    return keyboard_builder.as_markup(resize_keyboard=True)