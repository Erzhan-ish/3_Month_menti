from aiogram import types, Dispatcher
from aiogram.types import CallbackQuery
from bot_config import bot

async def address_callback(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Наш адрес Ибрагимова 103')
    await callback.answer()

def register_handler(dp: Dispatcher):
    dp.register_callback_query_handler(address_callback, lambda call: call.data == "address")