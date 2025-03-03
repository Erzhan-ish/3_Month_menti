import asyncio
from bot_config import dp, database
from handlers import (myinfo,
                      random,
                      start,
                      address,
                      hours,
                      review_dialog,
                      FSM_store)


async def main():
    start.register_handler(dp)
    random.register_handler(dp)
    myinfo.register_handler(dp)
    address.register_handler(dp)
    hours.register_handler(dp)
    review_dialog.register_handler(dp)
    FSM_store.register_handlers(dp)
    database.create_tables()
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
