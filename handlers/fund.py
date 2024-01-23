from aiogram import Router, F 
from aiogram.filters import Command
from aiogram.types import Message
from conf import *

from keyboards.base import getin 

router = Router()

@router.message(Command("start"))
async def hi(msg: Message):
    await msg.answer_animation(bf, caption=f"<b>Привет</b>, {msg.from_user.username}!\n<b>Какая радость, что ты пришел!</b>\n<i>Чтобы возпользоваться моими функциями, подпишись на канал:</i>", reply_markup=getin())

@router.message(F.animation)
async def get_gif(msg: Message):
    await msg.answer(msg.animation.file_id)