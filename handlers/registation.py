from aiogram import Router, F
from aiogram.enums.chat_type import ChatType
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from database.database import SessionLocal
from crud.operations import create_user,get_user,update_user
from keyboards.reply import keyboards as reply

router = Router()

@router.message(CommandStart(), F.chat.type == ChatType.PRIVATE)
async def registration(message: Message,command: Command, db = SessionLocal()):
    if (command.args is not None) and (command.args.isdigit() == True):
        owner_id = command.args
        owner = get_user(db,owner_id)
        update_user(user_id=command.args,refferals_count=owner.refferals_count + 1)
    else:
        owner_id = None
    user_id = message.from_user.id
    user_name = message.from_user.username or "NoUsername"
    full_name = message.from_user.full_name
    
    create_user(db, user_id, user_name, full_name,owner_id)
    
    await message.answer(f"""<b>👋 Привет! Я самый умный бот, \
у меня есть самые новейшие нейросети на данный момент!

Я буду незаменимым инструментом для вас. \
Используйте меня для учебы, работы и развлечений.</b>""",reply_markup=await reply.menu(message.from_user.id))
