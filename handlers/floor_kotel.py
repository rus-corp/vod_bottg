from aiogram import types, Router
from aiogram.types import CallbackQuery
from aiogram.filters.text import Text
from keyboards.inline_keyboard import choice_floor_kotel_power
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from vod_db_postgres.db_query import get_floor_kotels



router = Router()

@router.callback_query(Text(text='floor_kotels'))
async def kotel_power(callback: CallbackQuery):
    await callback.message.answer(text='Какая мощность Вам нужна?', reply_markup=choice_floor_kotel_power.as_markup())

@router.callback_query(Text(text='10kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='12.5kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='16kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='20kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='25kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='31.5kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='40kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='50kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='63kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='80kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='100kvtfl'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtfl', '')
    print(power)
    result = await get_floor_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))



