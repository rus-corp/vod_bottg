from aiogram import types, Router
from aiogram.types import CallbackQuery
from aiogram.filters.text import Text
from keyboards.inline_keyboard import choice_stena_kotel_power
from aiogram.utils.keyboard import ReplyKeyboardBuilder


from vod_db_postgres.db_query import get_wall_kotels

router = Router()

@router.callback_query(Text(text='stena_kotels'))
async def kotel_power(callback: CallbackQuery):
    await callback.message.answer(text='Какая мощность Вам нужна?', reply_markup=choice_stena_kotel_power.as_markup())


@router.callback_query(Text(text='10kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')
    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='11kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')
    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='13kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')

    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='16kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')

    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='18kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')

    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='20kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')

    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='24kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')

    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='28kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')

    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='32kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')

    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='36kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')

    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(text='40kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')

    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text(text='46kvtst'))
async def price_range(callback: CallbackQuery):    
    power=callback.data.replace('kvtst', '')

    result = await get_wall_kotels(power)
    builder = ReplyKeyboardBuilder()
    for item in result:
        builder.add(
            types.KeyboardButton(text=f'{item[0]} мощность {item[1]} цена-{item[2]}Тг', callback_data=item[0])
        )
        builder.adjust(1)
    await callback.message.answer('Выберите из списка ниже:', reply_markup=builder.as_markup(resize_keyboard=True))



