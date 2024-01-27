from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject, Command, StateFilter
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from conf import * 
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards.frst import based, true 

router = Router()


@router.message(Command("start"))
@router.message(CommandStart(deep_link=True,magic=F.args))
async def start_w(
         msg: Message,
        command: CommandObject,
):
    nem = command.args
    await msg.answer_animation(bf, caption="""
    <b>Привет!Я твоя Тян!</b>\nЯ очень рада, чтобы здесь<i>\nПодписывайся скорее на канал, а потом я отправлю название онямэ</i>""", 
    reply_markup=based())

@router.message(F.text == "Найти По Коду")
async def find(msg: Message):
    msg.answer("Gimme", reply_markup=ReplyKeyboardRemove())

@router.callback_query(F.data == "check")
async def check_sub(call: CallbackQuery):
    user = await call.bot.get_chat_member(chat_id='@tyan_corp', user_id=call.from_user.id)

    if user.status != 'left':
        await call.answer('Спасибо за подписку!')
        await call.message.delete()
        await call.message.answer_animation(i_gif, caption="<b>Спасибо!</b>\nЧто ты хочешь?", reply_markup=true())
        

    else:
        await call.answer('Для начала подпишись на наш канал')
@router.message()
async def ebash(msg: Message):
    msg.answer_animation(ebsh, caption="<b>ЕБААААААШЬ</b>")