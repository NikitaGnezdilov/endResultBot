from aiogram import Bot, Dispatcher
from app.handlers import router
from config import TOKEN
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    logging.info("Starting bot...")
    dp.include_router(router)
    await dp.start_polling(bot)
    logging.info("Bot started polling...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
