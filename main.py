import asyncio
import logging
from aiogram import Bot, Dispatcher
import database as db
from aiogram.fsm.context import FSMContext
from conf import *
from aiogram.types import Message
from aiogram import F
from aiogram.filters import CommandStart, CommandObject, Command
from handlers import user, hokage
from keyboards.base import based, hash
from handlers.user import Cher
async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=N, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(hokage.router, user.router)
    await bot.delete_webhook(drop_pending_updates=True)
    @dp.message(Command("start"))
    @dp.message(CommandStart(deep_link=True,magic=F.args))
    async def start_w(
            msg: Message,
            command: CommandObject,
            state: FSMContext
    ):
        nem = command.args
        await state.set_state(Cher.getid)
        await state.update_data(getid=nem)
        if msg.from_user.id in ADMINS: 
            await msg.answer_animation(g, caption="<b>А хули нам Хокагам</b>", reply_markup=hash())
        else:
            await msg.answer_animation(bf, caption="""
            <b>Привет! Я твоя Тян!</b>\nЯ очень рада, чтобы здесь<i>\nПодписывайся скорее на канал, а потом я отправлю название аниме</i>""", 
            reply_markup=based())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())