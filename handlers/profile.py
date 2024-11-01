from datetime import datetime
from aiogram import Router, F, Bot
from aiogram.enums.chat_type import ChatType
from states import states
from aiogram.types import Message,CallbackQuery
from database.database import SessionLocal
from aiogram.fsm.context import FSMContext
from crud.operations import get_user
from keyboards.inline import keyboards as inline
from utils.payments import create_cryptobot_invoice

router = Router()

@router.message(F.text == '📂 Профиль', F.chat.type == ChatType.PRIVATE)
async def profile(message: Message, db = SessionLocal()):
    user = get_user(db, message.from_user.id)
    registration_date = datetime.fromtimestamp(user.registeredAt).strftime('%d.%m.%Y')
    
    await message.answer(f"""📱 <b>Ваш профиль:</b>
<i>Основная информация:</i>

🔑 ID: <code>{message.from_user.id}</code>
🕜 Регистрация: <code>{registration_date}</code>

⚡️ Энергия: <code>{user.energy_count}</code>
💳 Баланс: <code>{user.balance} ₽</code>""",
                         reply_markup=await inline.profile())


@router.callback_query(F.data == 'profile')
async def profile_back(callback: CallbackQuery,bot: Bot, db = SessionLocal()):
    user = get_user(db, callback.from_user.id)
    registration_date = datetime.fromtimestamp(user.registeredAt).strftime('%d.%m.%Y')

    await bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.message_id,text=f"""📱 <b>Ваш профиль:</b>
<i>Основная информация:</i>

🔑 ID: <code>{callback.from_user.id}</code>
🕜 Регистрация: <code>{registration_date}</code>

⚡️ Энергия: <code>{user.energy_count}</code>
💳 Баланс: <code>{user.balance} ₽</code>""",reply_markup=await inline.profile())

@router.callback_query(F.data == 'refferals')
async def refferals(callback: CallbackQuery,bot: Bot, db = SessionLocal()):
    user = get_user(db, callback.from_user.id)
    bot_info = await bot.me()

    await bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.message_id,text=f"""<b>👨‍👩‍👧‍👦 Рефералы</b>
<i>Реферальная система позволит зарабатывать крупную сумму без вложений, Вам необходимо лишь делиться своей ссылкой.</i>

<b>🔗</b> Ссылка:  t.me/{bot_info.username}?start={callback.from_user.id}
<b>⚖️ Ставка:</b>  {user.refferals_percent}%

<b>👤 Приглашено:</b>  {user.refferals_count}
<b>💰 Пополнили:</b>  {user.refferals_deposit_count}
<b>🛍 Заработано:</b>  {user.refferals_earned} ₽""",reply_markup=await inline.profile_back())

    

@router.callback_query(F.data == 'deposit')
async def deposit(callback: CallbackQuery, bot: Bot, state: FSMContext, db = SessionLocal()):
    msg = await bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.message_id,text=f"""<b>💰 Пополнить баланс</b>
└ Сумма пополнения: <code>Не введена</code>

<i>♦️ Отправьте сумму пополнения или выберите один из предложенных вариантов.</i>""",reply_markup=await inline.deposit_amounts())
    await state.update_data(message_id = msg.message_id)
    await state.set_state(states.deposit.amount)



@router.message(states.deposit.amount)
async def enter_amount(message: Message, bot: Bot, state: FSMContext):
    await message.delete()
    data = await state.get_data()

    if message.text.replace('.', '', 1).isdigit() and message.text.count('.') <= 1:
        amount = float(message.text)
        if amount >= 1:
            await bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'],
                                          text=f"""<b>💰 Пополнить баланс</b>
├ Сумма пополнения:  <code>{amount} ₽</code>
└ Платежная система:  <code>Не выбрана</code>

<i>♦️ Выберите один из предложенных вариантов.</i>""",
                                          reply_markup=await inline.deposit_methods(amount))
        else:
            await bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'],
                                          text=f"""<b>❌ Некорректный ввод\n(<i>Сумма должна быть не менее 1 ₽</i>)</b>""",
                                          reply_markup=await inline.profile_back())
    else:
        await bot.edit_message_text(chat_id=message.chat.id, message_id=data['message_id'],
                                      text=f"""<b>❌ Некорректный ввод\n(<i>Отправьте число</i>)</b>""",
                                      reply_markup=await inline.profile_back())
    await state.clear()

@router.callback_query(F.data.startswith('methods'))
@router.callback_query(F.data.startswith('amount'))
async def deposit(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.clear()
    amount = float(callback.data.split('|')[1])
    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                        text=f"""<b>💰 Пополнить баланс</b>
├ Сумма пополнения:  <code>{amount} ₽</code>
└ Платежная система:  <code>Не выбрана</code>

<i>♦️ Выберите один из предложенных вариантов.</i>""",
                                        reply_markup=await inline.deposit_methods(amount))  
    


@router.callback_query(F.data.startswith('payment_method'))
async def deposit(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.clear()
    amount = float(callback.data.split('|')[2])
    url = await create_cryptobot_invoice(amount)

    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                        text=f"""<b>💰 Пополнить баланс</b>
├ Сумма пополнения:  <code>{amount} ₽</code>
└ Платежная система:  <code>{callback.data.split('|')[1]} </code>

<i>❔ После оплаты средства будут автоматически зачислены на баланс.</i>

<b>☹️ Платёж не дошёл или другая проблема?</b>
<i>Обратитесь в техническую поддержку с подробным описанием вашей проблемы..</i>""",
                                        reply_markup=await inline.payment_buttons(amount,url))
    
