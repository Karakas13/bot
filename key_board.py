from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from states import UserStates


def get_keyboard(buttons):
    kb = []
    for button in buttons:
        kb.append([KeyboardButton(text=button)])
    reply_markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return reply_markup

keyboards = {
    UserStates.BASE: get_keyboard(["Мои пари", "Создать пари"]),
    UserStates.CREATING_PARI: get_keyboard(["Отмена"])
}