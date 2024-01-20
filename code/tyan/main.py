import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from tkn import TKN

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TKN)
# Диспетчер
dp = Dispatcher()

#ебашем фильтр для проерки подписки

@dp.message(Command("start"))
async def cmd_start(msg: types.Message):
    res = await bot.get_chat_member(chat_id="@tyan_corp", user_id=msg.from_user.id)
    await msg.answer(res.status)


async def main():
    await dp.start_polling(bot)

@dp.message()
async def all(msg: types.Message):
    await msg.answer("ТУТ МНОГО ДРОЧЕВА И ДЕНЕГ")
    
if __name__ == "__main__":
    asyncio.run(main())