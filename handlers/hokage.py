from aiogram import Router, F
from filters.isa import IsAdmin
from aiogram.filters import Command
from aiogram.types import Message
from conf import * 

router = Router()

@router.message(IsAdmin())
async def all(msg: Message):
    msg.answer_animation(i_gif, caption="<i>my hookage</i>")