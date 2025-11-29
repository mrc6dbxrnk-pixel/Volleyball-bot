from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from database import db
from keyboards.user_kb import shift_list_kb, shift_actions_kb

router = Router()

@router.message(F.text == "/start")
async def start(message: Message):
    conn=db(); cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (tg_id, username, full_name) VALUES (?, ?, ?)",
        (message.from_user.id, message.from_user.username, message.from_user.full_name))
    conn.commit(); conn.close()
    await message.answer("Привет! Чтобы посмотреть смены: /shifts")

@router.message(F.text == "/shifts")
async def show_shifts(message: Message):
    conn=db(); cur=conn.cursor()
    cur.execute("SELECT id, date, time_label, price FROM shifts ORDER BY id DESC")
    shifts=cur.fetchall(); conn.close()
    if not shifts:
        await message.answer("Нет смен.")
        return
    await message.answer("Выберите смену:", reply_markup=shift_list_kb(shifts))

@router.callback_query(F.data.startswith("shift_"))
async def open_shift(call: CallbackQuery):
    shift_id=call.data.split("_")[1]
    conn=db(); cur=conn.cursor()
    cur.execute("SELECT date, time_label, price FROM shifts WHERE id=?", (shift_id,))
    shift=cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM registrations WHERE shift_id=? AND status='plus'", (shift_id,))
    plus_count=cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM registrations WHERE shift_id=? AND paid=1", (shift_id,))
    paid_count=cur.fetchone()[0]
    conn.close()
    text=f"📅 {shift[0]}\n⏰ {shift[1]}\n💵 {shift[2]} сум\n\n➕ Записались: {plus_count}\n💳 Оплатили: {paid_count}"
    await call.message.edit_text(text, reply_markup=shift_actions_kb(shift_id))
