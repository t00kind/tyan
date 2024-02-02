from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from conf import * 
from typing import Union
from keyboards.base import hash, bash
from aiogram.filters import BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database import add_all, get_all


class IsAdmin(BaseFilter):

    async def __call__(self, msg: Message) -> bool:
        return msg.from_user.id in ADMINS

class AddAnime(StatesGroup):
    name = State()
    desc = State()
    photo = State()
    author = State()
    code = State()
    
router = Router()
router.message.filter(IsAdmin())
@router.message(Command("cancel"))
async def stopi(msg: Message, state: FSMContext):
    await state.clear()

@router.message(AddAnime.name)
async def get_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("<b>Хорошо, теперь описание</b>")
    await state.set_state(AddAnime.desc)

@router.message(AddAnime.desc)
async def get_name(msg: Message, state: FSMContext):
    await state.update_data(desc=msg.text)
    await msg.answer("<b>Пришлите фото</b>")
    await state.set_state(AddAnime.photo)

@router.message(AddAnime.photo, F.photo)
async def get_name(msg: Message, state: FSMContext):
    await state.update_data(photo=msg.photo[0].file_id)
    await msg.answer("<b>Название студии/имя автора</b>")
    await state.set_state(AddAnime.author)

@router.message(AddAnime.author)
async def get_name(msg: Message, state: FSMContext):
    await state.update_data(author=msg.text)
    await msg.answer("<b>Уникальное 3х значное число</b>")
    await state.set_state(AddAnime.code)
@router.message(AddAnime.code)
async def get_name(msg: Message, state: FSMContext):
    await state.update_data(code=msg.text)
    data = await state.get_data()
    await add_all(data)
    await state.clear()
    kode = data["code"]
    await msg.answer("<b>Успех!</b> 🦾")
    await msg.answer(f"Ссылка: https://t.me/an1tyan_bot?start={kode}")
    

@router.message(Command("start"))
@router.message(F.text)
async def adm(msg: Message):
    await msg.answer_animation(g, caption="<b>А хули нам Хокагам</b>", reply_markup=hash())

@router.callback_query(F.data == "add")
async def add(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Для отмены введите /cancel")
    await call.message.answer("<b>Введите название</b>")
    await state.set_state(AddAnime.name)
    await call.answer()

@router.callback_query(F.data == "pop")
async def add(call: CallbackQuery):
    g = get_all()
    res = ""

    for i in g:
        name = i[0]
        code = i[4]
        res += f"\n<code>{name}</code> \n"
    got = "<b>Все что есть в Базе:</b>\n" + res
    await call.message.answer_animation(ebsh, caption=got)
    await call.answer()


@router.callback_query(F.data == "switch")
async def switch(call: CallbackQuery):
    ADMINS.remove(call.from_user.id)
    await call.message.delete()
    await call.message.answer("Чтобы вновь стать Хокаге, введите команду /h, или нажмите на кнопку", reply_markup=bash())
    await call.answer()



