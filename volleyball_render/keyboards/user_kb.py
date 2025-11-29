from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def shift_list_kb(shifts):
    kb=[]
    for s in shifts:
        kb.append([InlineKeyboardButton(
            text=f"{s[1]} • {s[2]} • {s[3]} сум",
            callback_data=f"shift_{s[0]}"
        )])
    return InlineKeyboardMarkup(inline_keyboard=kb)

def shift_actions_kb(id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ Иду", callback_data=f"plus_{id}")],
        [InlineKeyboardButton(text="➖ Не иду", callback_data=f"minus_{id}")],
        [InlineKeyboardButton(text="💳 Оплатить 50%", callback_data=f"pay_{id}")]
    ])
