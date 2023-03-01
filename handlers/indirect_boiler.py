from aiogram import types, Router
from aiogram.types import CallbackQuery
from aiogram.filters.text import Text
from keyboards.inline_keyboard import choice_indirect_boiler_vol
from aiogram.utils.keyboard import ReplyKeyboardBuilder


from vod_db_postgres.db_query import get_indirect_boiler

router = Router()

@router.callback_query(Text(text='indirect_boiler'))
async def kotel_power(callback: CallbackQuery):
    await callback.message.answer(text='Какая объем Вам нужен?', reply_markup=choice_indirect_boiler_vol.as_markup())

@router.callback_query(Text(text='80liters'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('liters', '')
    result = await get_indirect_boiler(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='100liters'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('liters', '')
    result = await get_indirect_boiler(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='120liters'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('liters', '')
    result = await get_indirect_boiler(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='140liters'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('liters', '')
    result = await get_indirect_boiler(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='200liters'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('liters', '')
    result = await get_indirect_boiler(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='250liters'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('liters', '')
    result = await get_indirect_boiler(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='300liters'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('liters', '')
    result = await get_indirect_boiler(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='400liters'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('liters', '')
    result = await get_indirect_boiler(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='500liters'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('liters', '')
    result = await get_indirect_boiler(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))
