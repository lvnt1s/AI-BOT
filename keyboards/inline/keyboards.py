from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder,KeyboardBuilder
from aiogram.types import InlineKeyboardButton,KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import json
import ast


async def information():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.row(
        InlineKeyboardButton(text="👨‍💻 Администратор",url = 't.me/babydrainy')
    )
    keyboard_builder.row(
        InlineKeyboardButton(text="🛠 Тех. поддержка",url = 't.me/babydrainy'),
        InlineKeyboardButton(text="🌐 Все проекты",url = 't.me/babydrainy')
    )
    keyboard_builder.row(
        InlineKeyboardButton(text="📄 Пользовательское соглашение",url = 't.me/babydrainy')
    )
    return keyboard_builder.as_markup()

async def profile():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.row(
        InlineKeyboardButton(text="💰 Пополнить баланс",callback_data = 'deposit')
    )
    keyboard_builder.row(
        InlineKeyboardButton(text="🎟 Купоны",callback_data = 'coupons'),
        InlineKeyboardButton(text="👨‍👩‍👦‍👦 Рефералы",callback_data = 'refferals')
    )
    keyboard_builder.row(
        InlineKeyboardButton(text="⚡️ Купить энергию",callback_data = 'buy_energy')
    )
    return keyboard_builder.as_markup()


async def profile_back():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text = '◀️ Вернуться',callback_data = 'profile'))
    builder.adjust(3,3,3,1,1)
    return builder.as_markup()

async def deposit_amounts():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text = '30 ₽',callback_data = 'amount|30'))
    builder.row(InlineKeyboardButton(text = '50 ₽',callback_data = 'amount|50'))
    builder.row(InlineKeyboardButton(text = '60 ₽',callback_data = 'amount|60'))
    builder.row(InlineKeyboardButton(text = '100 ₽',callback_data = 'amount|100'))
    builder.row(InlineKeyboardButton(text = '200 ₽',callback_data = 'amount|200'))
    builder.row(InlineKeyboardButton(text = '300 ₽',callback_data = 'amount|300'))
    builder.row(InlineKeyboardButton(text = '500 ₽',callback_data = 'amount|500'))
    builder.row(InlineKeyboardButton(text = '800 ₽',callback_data = 'amount|800'))
    builder.row(InlineKeyboardButton(text = '1500 ₽',callback_data = 'amount|1500'))
    builder.row(InlineKeyboardButton(text = '◀️ Вернуться',callback_data = 'profile'))
    builder.adjust(3,3,3,1)
    return builder.as_markup()

async def deposit_methods(amount):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text = '💜 AAIO',callback_data = f'payment_method|💜 AAIO|{amount}'))
    builder.row(InlineKeyboardButton(text = '💎 CrystalPay',callback_data = f'payment_method|💎 CrystalPay|{amount}'))
    builder.row(InlineKeyboardButton(text = '💠 Cryptobot',callback_data = f'payment_method|💠 Cryptobot|{amount}'))
    builder.row(InlineKeyboardButton(text = '👁 LOLZ',callback_data = f'amount|👁 LOLZ|{amount}'))
    builder.row(InlineKeyboardButton(text = '◀️ Вернуться',callback_data = 'deposit'))
    builder.adjust(2,2,1)
    return builder.as_markup()

async def payment_buttons(amount,url):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text = '🔥 Перейти к оплате',url = url))
    builder.row(InlineKeyboardButton(text = '🆘 Техническая поддержка',url = f't.me/babydrainy'))
    builder.row(InlineKeyboardButton(text = '◀️ Вернуться',callback_data = f'methods|{amount}'))
    builder.adjust(2,1)
    return builder.as_markup()


