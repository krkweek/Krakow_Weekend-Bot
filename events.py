from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

def register_event_handlers(dp):
    dp.include_router(router)

@router.message(Command("new_event"))
async def new_event(message: Message):
    await message.answer("Создание мероприятий пока в разработке. В будущих версиях будет поддержка кнопок и регистрации.")
