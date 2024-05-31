import asyncio
from aiogram import Bot, Dispatcher

from handlers import user
from admin import admin


async def main():
    bot = Bot(token='TOKEN')
    dp = Dispatcher()
    dp.include_routers(user, admin)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
