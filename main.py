from asyncio import run
import logging 
from aiogram import F 

from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import hide_link

from aiogram.filters.command import Command
from conf import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TKN, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(msg: types.Message):
    kb = [
        [types.KeyboardButton(text="Хочу аниме")],
        [types.KeyboardButton(text="Хочу мангу")]
    ]
    keyb = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите тип")
    await msg.answer_animation(bf, caption="<b>Привет!\nЭто ANITYAN</b>", reply_markup=keyb)
async def main():
    await dp.start_polling(bot)

@dp.message(F.text.lower() == "хочу аниме")
async def with_puree(message: types.Message):
    await message.reply_animation(sm, caption="Уроки учи")

@dp.message(F.text.lower() == "хочу мангу")
async def without_puree(message: types.Message):
    await message.reply_animation(ebsh, caption="Только так побеждают!")

@dp.message(F.animation)
async def echo_gif(msg: types.Message):
    await msg.reply(f"{msg.animation.file_id}")

@dp.message()
async def base(msg: types.Message):
    await msg.answer_animation(i_gif, caption="<b>Замолчи</b>\n<i>Омае Юай</i>")

if __name__ == "__main__":
    run(main())
