import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message




import os

logging.basicConfig(level=logging.INFO)

from config import token


bot = Bot(token=token)
dp = Dispatcher()




async def main():
    from handlers import user, wall_kotels, floor_kotel, chimney, water_heater, circul_pump, exp_tanker, heat_floor, indirect_boiler, station_pump
    dp.include_router(user.router)
    dp.include_router(wall_kotels.router)
    dp.include_router(floor_kotel.router)
    dp.include_router(chimney.router)
    dp.include_router(water_heater.router)
    dp.include_router(circul_pump.router)
    dp.include_router(exp_tanker.router)
    dp.include_router(heat_floor.router)
    dp.include_router(indirect_boiler.router)
    dp.include_router(station_pump.router) 

    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())

