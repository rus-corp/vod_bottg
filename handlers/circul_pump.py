from aiogram import types, Router
from aiogram.types import CallbackQuery
from aiogram.filters.text import Text
from keyboards.inline_keyboard import choice_circ_pump
from aiogram.utils.keyboard import ReplyKeyboardBuilder


from vod_db_postgres.db_query import get_circ_pump

router = Router()

@router.callback_query(Text(text='circ_pump'))
async def kotel_power(callback: CallbackQuery):
    await callback.message.answer(text='Какой присоединительный размер?', reply_markup=choice_circ_pump.as_markup())


@router.callback_query(Text(text='25d'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('d', '')
    result = await get_circ_pump(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} диаметр {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))



@router.callback_query(Text(text='30d'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('d', '')
    result = await get_circ_pump(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} диаметр {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='32d'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('d', '')
    result = await get_circ_pump(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} диаметр {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='45d'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('d', '')
    result = await get_circ_pump(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} диаметр {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='253d'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('d', '')
    result = await get_circ_pump(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} диаметр {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


