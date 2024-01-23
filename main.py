from asyncio import run
import logging 
from handlers import fund
from aiogram import Bot, Dispatcher


from conf import TKN

logging.basicConfig(level=logging.INFO)
async def main():
    bot = Bot(token=TKN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(fund.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    run(main())
