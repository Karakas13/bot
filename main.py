from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F
from aiogram.filters.state import StateFilter
from states import UserStates
from key_board import keyboards

import pari_service as ps

from config import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message, state:FSMContext):
    kb = keyboards[UserStates.BASE]
    await bot.send_message(message.chat.id, "Привет! Я эхо-бот", reply_markup=kb)
    await  state.set_state(UserStates.BASE)


@dp.message((F.text == "Мои пари"), StateFilter(UserStates.BASE))
async def my_paris(message: types.Message):
    text = "Твои пари"
    paris = ps.get_paris(message.from_user.id)
    for pari in paris:
        text += "\n" + pari
    await message.answer(text)

@dp.message((F.text == "Создать пари"), StateFilter(UserStates.BASE))
async def start(message: types.Message):
    text = ps.add_pari(message.from_user.id, message.text)
    await message.answer(text)

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
