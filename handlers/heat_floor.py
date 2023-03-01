from aiogram import types, Router
from aiogram.types import CallbackQuery
from aiogram.filters.text import Text

from aiogram.utils.keyboard import ReplyKeyboardBuilder


from vod_db_postgres.db_query import get_heat_floor

router = Router()

@router.callback_query(Text(text='heating_floor'))
async def kotel_power(callback: CallbackQuery):
    result = await get_heat_floor()
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже: ', reply_markup=builder.as_markup(resize_keyboard=True))
    