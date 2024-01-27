import asyncio
import logging
from aiogram import Bot, Dispatcher

from conf import N
from handlers import user, hokage


logging.basicConfig(level=logging.INFO)
async def main():
    bot = Bot(token=N, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(hokage.router, user.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())