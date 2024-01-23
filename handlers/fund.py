from aiogram import Router, F 
from aiogram.filters import Command
from aiogram.types import Message
from conf import *

from keyboards.base import getin 

router = Router()

@router.message(Command("start"))
async def hi(msg: Message):
    user_channel_status = await msg.get_chat_member(chat_id="@tyan_corp", user_id=msg.chat.id)
    user_channel_status = re.findall(r"\w*", str(user_channel_status))
    try:
        if user_channel_status[70] != 'left':
           await msg.anwer("oh, it woaaarks")
        else:
            await msg.anwer("oh, it woddrks")
            #Условие для тех, кто не подписан
    except:
        if user_channel_status[60] != 'left':
            await msg.anwer("oh, it workss")
            #Условие для "подписанных"
        else:
            await msg.anwer("oh, it wordks")
    await msg.answer_animation(bf, caption=f"<b>Привет</b>, {msg.from_user.username}!\n<b>Какая радость, что ты пришел!</b>\n<i>Чтобы возпользоваться моими функциями, подпишись на канал:</i>", reply_markup=getin())

@router.message(F.animation)
async def get_gif(msg: Message):
    await msg.answer(msg.animation.file_id)