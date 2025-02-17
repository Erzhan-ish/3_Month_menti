import asyncio
from bot_config import dp
from handlers import (myinfo,
                      random,
                      start,
                      address,
                      hours)


async def main():
    start.register_handler(dp)
    random.register_handler(dp)
    myinfo.register_handler(dp)
    address.register_handler(dp)
    hours.register_handler(dp)
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
