from aiogram import types, Router
from aiogram.types import CallbackQuery
from aiogram.filters.text import Text
from keyboards.inline_keyboard import choice_heater_volume
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from vod_db_postgres.db_query import get_el_water_heater


router = Router()


@router.callback_query(Text(text='water_heater'))
async def kotel_power(callback: CallbackQuery):
    await callback.message.answer(text='Какой объем Вам нужен?', reply_markup=choice_heater_volume.as_markup())



@router.callback_query(Text(text='10lit'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('lit', '')
    result = await get_el_water_heater(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже: ', reply_markup=builder.as_markup(resize_keyboard=True))



@router.callback_query(Text(text='15lit'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('lit', '')
    result = await get_el_water_heater(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='20lit'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('lit', '')
    result = await get_el_water_heater(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='30lit'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('lit', '')
    result = await get_el_water_heater(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='50lit'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('lit', '')
    result = await get_el_water_heater(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='65lit'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('lit', '')
    result = await get_el_water_heater(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='80lit'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('lit', '')
    result = await get_el_water_heater(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='100lit'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('lit', '')
    result = await get_el_water_heater(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))
