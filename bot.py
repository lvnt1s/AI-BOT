import asyncio

from aiogram import Bot, Dispatcher
import logging
from handlers import registation,information,profile
import sys
import logging
from aiogram.exceptions import  TelegramConflictError
from aiogram.types import FSInputFile  
from core.config_reader import settings
import logging
from database.database import engine, Base
from aiogram.client.default import DefaultBotProperties



async def main():
    Base.metadata.create_all(bind=engine)

    bots = [Bot(
        settings.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode="HTML",
                                     link_preview_is_disabled=True)
    )]
    
    dispatcher = Dispatcher()
    dispatcher.include_routers(registation.router,information.router,profile.router)
    try:
        await dispatcher.start_polling(*bots, allowed_updates=["message", "inline_query", "chat_member", "my_chat_member","callback_query"])
    except TelegramConflictError:
        pass
    

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
