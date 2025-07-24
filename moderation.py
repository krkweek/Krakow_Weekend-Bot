from aiogram import Router, F
from aiogram.types import Message
from config import ADMINS

router = Router()

def register_moderation_handlers(dp):
    dp.include_router(router)

@router.message(F.text.contains("http") | F.text.contains("t.me"))
async def delete_links(message: Message):
    if message.from_user.id not in ADMINS:
        await message.delete()
        await message.answer("❗ В чате запрещена реклама и ссылки.")
