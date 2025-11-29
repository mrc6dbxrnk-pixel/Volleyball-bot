from aiogram import Router
from aiogram.types import Message
from database import db

router = Router()

@router.message()
async def payment_check(message: Message):
    if not message.photo:
        return
    conn=db(); cur=conn.cursor()
    cur.execute("UPDATE registrations SET screenshot_id=?, paid=0 WHERE user_id=(SELECT id FROM users WHERE tg_id=?)",
                (message.photo[-1].file_id, message.from_user.id))
    conn.commit(); conn.close()
    await message.answer("Чек отправлен. Ожидайте подтверждения.")
