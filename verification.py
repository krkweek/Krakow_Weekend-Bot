from aiogram import Router, F
from aiogram.types import Message
from config import CHAT_ID

router = Router()

def register_verification_handlers(dp):
    dp.include_router(router)

@router.message(F.chat.type == "private")
async def handle_verification(message: Message):
    await message.answer("Привет! Укажи имя, возраст и немного о себе. После проверки тебя добавят в Krakow Weekend.\n❗ В чате запрещена реклама и ссылки.")
