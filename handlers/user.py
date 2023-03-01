
from aiogram import types, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command


from aiogram.filters.text import Text
from keyboards.inline_keyboard import main_menu, catalog_menu
from run_bot import dp, bot

import time

from aiogram.utils.keyboard import ReplyKeyboardBuilder




router = Router()


@router.message(Command(commands=['start']))
async def show_menu(message: types.Message):
    await message.answer(f'Здравствуйте {message.from_user.first_name}, добро пожаловать к нам в магазин! Взягляните на наш каталог', reply_markup=main_menu.as_markup())


@router.callback_query(Text(text='catalog'))
async def catalog_coma(callback: types.CallbackQuery):
    await callback.message.answer(text='Отлично', reply_markup=catalog_menu.as_markup())









    

