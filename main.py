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
import storage_user_repository as storage

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def send_welcome(message: types.Message, state:FSMContext):
    user_storage.save_user(message.from_user.username message.chat.id)
    print(message.from_user.username)
    print(message.chat.id)
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
async def add_pari(message: types.Message, state FSMContext):
    text = ps.set_pari_name()
    await message.answer(text)
    await states.set_states(UserStates.CREATING_PARI)




@dp.message(StateFilter(UserStates.CREATING_PARI))
async def set_paro_name(message: types.Message state: FSMContext):
    text = ps.set_pary_taker()
    await message.answer(text)



@dp.message(StateFilter(UserStates.CREATING_PARI))
async  def set_pari_name(message: types_Message, states)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
