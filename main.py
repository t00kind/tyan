from asyncio import run
import logging 
from aiogram import F 

from aiogram import Bot, Dispatcher, types

from aiogram.filters.command import Command
from conf import TKN, i_gif, bf

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TKN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer_animation(bf, caption="<b>Привет!\nЭто ANITYAN</b>")

async def main():
    await dp.start_polling(bot)

@dp.message(F.animation)
async def echo_gif(msg: types.Message):
    await msg.reply(f"{msg.animation.file_id}")

@dp.message()
async def base(msg: types.Message):
    await msg.answer_animation(i_gif, caption="<b>Замолчи</b>\n<i>Омае Юай</i>")
if __name__ == "__main__":
    run(main())
