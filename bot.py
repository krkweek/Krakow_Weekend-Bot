import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.verification import register_verification_handlers
from handlers.moderation import register_moderation_handlers
from handlers.events import register_event_handlers
from handlers.utils import register_util_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

register_verification_handlers(dp)
register_moderation_handlers(dp)
register_event_handlers(dp)
register_util_handlers(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
