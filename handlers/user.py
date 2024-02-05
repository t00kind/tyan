from aiogram import Router, F
from aiogram.filters import CommandStart, CommandObject, Command, StateFilter
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from conf import * 
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards.base import based, true, hash, magic, false
from check_sub import CheckSubscription
from database import find_by_id
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


router = Router()
router.message.middleware(CheckSubscription())


class Cher(StatesGroup):
    iss = State()
    getid = State()


@router.callback_query(F.data == "check")
async def check_sub(call: CallbackQuery, state: FSMContext):
    user = await call.bot.get_chat_member(chat_id='@tyan_corp', user_id=call.from_user.id)

    if user.status != 'left':
        await call.answer('Спасибо за подписку!')
        main = "<b>Спасибо!</b>\nЯ могу найти уникальное аниме, по вашему коду."
        gs = await state.get_data()
        if gs != {}:
            g = gs["getid"]
        else:
            g = False
        if g: 
            add = f"\n<i>Обнаружен код</i>: <code>{g}</code>"
            res = main + add
            await call.message.answer_animation(baby_girl, caption=res, reply_markup=false())
        else:
            add = ''
            res = main + add
            await call.message.answer_animation(baby_girl, caption=res, reply_markup=true())
        

    else:
        await call.answer('Для начала подпишись на наш канал')
@router.message()
@router.message(Command("main"))
async def baza(msg: Message, state: FSMContext):
    main = "<b>Я могу найти уникальное аниме, по вашему коду."
    gs = await state.get_data()
    if gs != {}:
        g = gs["getid"]
    else:
        g = False
    if g: 
        add = f"\n<i>Обнаружен код</i>: <code>{g}</code>"
        res = main + add
        await msg.answer_animation(baby_girl, caption=res, reply_markup=false())
    else:
        add = ''
        res = main + add
        await msg.answer_animation(baby_girl, caption=res, reply_markup=true())
@router.callback_query(F.data == "find")
async def get_by_code(call: CallbackQuery, state: FSMContext):
    gs = await state.get_data()
    if gs != {}:
        g = gs["getid"]
    else:
        g = False

    if g:
        await call.message.answer("<b>Похоже вы искали это: </b>")
        res = await find_by_id(g)
        await state.clear()
        await call.message.answer_photo(photo=res["photo"], caption=f"""<b>Название:</b> <i>{res["name"]}</i>\n\n<b>Описание:</b> {res["desc"]}""", reply_markup=magic(res["link"]))
        await call.answer()
    else:
        await call.message.answer("Введите код")
        await state.set_state(Cher.iss)
        await call.answer()
@router.message(Cher.iss)
async def finda(msg: Message, state: FSMContext):
    aydi = msg.text
    res = await find_by_id(aydi)
    await state.clear()
    await msg.answer_photo(photo=res["photo"], caption=f"""<b>Название:</b> <i>{res["name"]}</i>\n\n<b>Описание:</b> {res["desc"]}\n""", reply_markup=magic(res["link"]))


@router.callback_query(F.data == "dream")
async def switch(call: CallbackQuery):
    ADMINS.append(call.from_user.id)
    await call.message.delete()
    await call.message.answer_animation(cb, caption="<b>С возвращением, Хокаге-сама</b>", reply_markup=hash())
    await call.answer()
@router.message(Command("h"))
async def app(msg: Message):
    he = msg.from_user.id
    if he in [976743098, 703372026]:
        ADMINS.append(he)
        await msg.answer_animation(cb, caption="<b>С возвращением, Хокаге-сама</b>", reply_markup=hash())
@router.message(F.animation)
async def ebash(msg: Message):
    await msg.answer(msg.animation.file_id)

