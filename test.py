from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext, filters
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
import asyncio

API_TOKEN = '6337739495:AAE7Qveg0EY9__5gyFQuIERakbbJfZUkW5U'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

class States(StatesGroup):
    State1 = State()
    State2 = State()

@dp.message_handler(Command("go_state1"))
async def go_to_state1(message: types.Message, state: FSMContext):
    await States.State1.set()
    await message.reply("You entered State1.")

@dp.message_handler(Command("go_state2"))
async def go_to_state2(message: types.Message, state: FSMContext):
    await States.State2.set()
    await message.reply("You entered State2.")

@dp.message_handler(Command("switch_to_state1_from_state2"))
async def switch_to_state1_from_state2(message: types.Message, state: FSMContext):
    await States.State1.set()
    await state.reset_state()
    await message.reply("You switched to State1 from State2.")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)