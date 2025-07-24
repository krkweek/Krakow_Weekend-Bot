from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

def register_util_handlers(dp):
    dp.include_router(router)

@router.message(Command("ping_all"))
async def ping_all(message: Message):
    await message.answer("⛔ Массовое упоминание временно недоступно. Telegram ограничивает упоминания. Будет реализовано частично в будущем.")
