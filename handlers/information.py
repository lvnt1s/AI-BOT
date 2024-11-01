from aiogram import Router, F
from aiogram.enums.chat_type import ChatType
from aiogram.types import Message
from keyboards.inline import keyboards as inline

router = Router()

@router.message(F.text == 'ℹ️ Информация', F.chat.type == ChatType.PRIVATE)
async def information(message: Message,):
    await message.answer(f"""<b>ℹ️ Информация</b>""",
                         reply_markup=await inline.information())
