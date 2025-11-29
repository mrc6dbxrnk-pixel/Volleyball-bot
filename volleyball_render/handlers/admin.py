from aiogram import Router, F
from aiogram.types import Message
from config import ADMIN_ID
from keyboards.admin_kb import admin_main_kb

router = Router()

@router.message(F.text == "/admin")
async def admin_panel(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    await message.answer("Админ панель:", reply_markup=admin_main_kb())
