from aiogram import types, Router
from aiogram.types import CallbackQuery
from aiogram.filters.text import Text
from keyboards.inline_keyboard import choice_exp_tank_vol
from aiogram.utils.keyboard import ReplyKeyboardBuilder


from vod_db_postgres.db_query import get_exp_tank

router = Router()

@router.callback_query(Text(text='exp_tank'))
async def kotel_power(callback: CallbackQuery):
    await callback.message.answer(text='Какой объем нужен?', reply_markup=choice_exp_tank_vol.as_markup())

@router.callback_query(Text(text='8vol'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('vol', '')
    result = await get_exp_tank(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='12vol'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('vol', '')
    result = await get_exp_tank(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='35vol'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('vol', '')
    result = await get_exp_tank(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='50vol'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('vol', '')
    result = await get_exp_tank(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='150vol'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('vol', '')
    result = await get_exp_tank(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} объем {item[1]}л цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))
