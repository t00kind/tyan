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


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("ПЕНИСЫ")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
@dp.message()
async def all(msg: types.Message):
    await msg.answer("ТУТ БУДЕТ МНОГО ДРОЧЕВА И ДЕНЕГ")
if __name__ == "__main__":
    asyncio.run(main())