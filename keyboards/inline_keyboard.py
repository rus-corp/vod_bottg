from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


main_menu = InlineKeyboardBuilder()
main_menu.add(types.inline_keyboard_button.InlineKeyboardButton(
    text='Каталог', callback_data='catalog'))


catalog_menu = InlineKeyboardBuilder()
catalog_menu.add(types.InlineKeyboardButton(text='Настенные котлы', callback_data='stena_kotels'),
                 types.InlineKeyboardButton(
                     text='Напольные котлы', callback_data='floor_kotels'),
                 types.InlineKeyboardButton(
    text='Дымоходы', callback_data='dimohod'),
    types.InlineKeyboardButton(
    text='Водонагреватели', callback_data='water_heater'),
    types.InlineKeyboardButton(
    text='Циркуляционные насосы', callback_data='circ_pump'),
    types.InlineKeyboardButton(
    text='Теплый пол', callback_data='heating_floor'),
    types.InlineKeyboardButton(
    text='Расширительные баки', callback_data='exp_tank'),
    types.InlineKeyboardButton(
    text='Насосные станции и Дренажные насосы', callback_data='station_pump'),
    types.InlineKeyboardButton(
    text='Косвенные бойлера', callback_data='indirect_boiler')

)
catalog_menu.adjust(1)


choice_stena_kotel_power = InlineKeyboardBuilder()
choice_stena_kotel_power.add(
    types.InlineKeyboardButton(text='10 кВт', callback_data='10kvtst'),
    types.InlineKeyboardButton(text='11 кВт', callback_data='11kvtst'),
    types.InlineKeyboardButton(text='13 кВт', callback_data='13kvtst'),
    types.InlineKeyboardButton(text='16 кВт', callback_data='16kvtst'),
    types.InlineKeyboardButton(text='18 кВт', callback_data='18kvtst'),
    types.InlineKeyboardButton(text='20 кВт', callback_data='20kvtst'),
    types.InlineKeyboardButton(text='24 кВт', callback_data='24kvtst'),
    types.InlineKeyboardButton(text='28 кВт', callback_data='28kvtst'),
    types.InlineKeyboardButton(text='32 кВт', callback_data='32kvtst'),
    types.InlineKeyboardButton(text='36 кВт', callback_data='36kvtst'),
    types.InlineKeyboardButton(text='40 кВт', callback_data='40kvtst'),
    types.InlineKeyboardButton(text='46 кВт', callback_data='46kvtst'),
)
choice_stena_kotel_power.adjust(4)


choice_floor_kotel_power = InlineKeyboardBuilder()
choice_floor_kotel_power.add(
    types.InlineKeyboardButton(text='10 кВт', callback_data='10kvtfl'),
    types.InlineKeyboardButton(text='12,5 кВт', callback_data='12.5kvtfl'),
    types.InlineKeyboardButton(text='16 кВт', callback_data='16kvtfl'),
    types.InlineKeyboardButton(text='20 кВт', callback_data='20kvtfl'),
    types.InlineKeyboardButton(text='25 кВт', callback_data='25kvtfl'),
    types.InlineKeyboardButton(text='31,5 кВт', callback_data='31.5kvtfl'),
    types.InlineKeyboardButton(text='40 кВт', callback_data='40kvtfl'),
    types.InlineKeyboardButton(text='50 кВт', callback_data='50kvtfl'),
    types.InlineKeyboardButton(text='63 кВт', callback_data='63kvtfl'),
    types.InlineKeyboardButton(text='80 кВт', callback_data='80kvtfl'),
    types.InlineKeyboardButton(text='100 кВт', callback_data='100kvtfl'),
)
choice_floor_kotel_power.adjust(4)

choice_heater_volume = InlineKeyboardBuilder()
choice_heater_volume.add(
    types.InlineKeyboardButton(text='10л', callback_data='10lit'),
    types.InlineKeyboardButton(text='15л', callback_data='15lit'),
    types.InlineKeyboardButton(text='20л', callback_data='20lit'),
    types.InlineKeyboardButton(text='30л', callback_data='30lit'),
    types.InlineKeyboardButton(text='50л', callback_data='50lit'),
    types.InlineKeyboardButton(text='65л', callback_data='65lit'),
    types.InlineKeyboardButton(text='80л', callback_data='80lit'),
    types.InlineKeyboardButton(text='100л', callback_data='100lit')
)
choice_heater_volume.adjust(4)

choice_circ_pump = InlineKeyboardBuilder()
choice_circ_pump.add(
    types.InlineKeyboardButton(text='25', callback_data='25d'),
    types.InlineKeyboardButton(text='30', callback_data='30d'),
    types.InlineKeyboardButton(text='32', callback_data='32d'),
    types.InlineKeyboardButton(text='45', callback_data='45d'),
    types.InlineKeyboardButton(text='253', callback_data='253d')
)
choice_circ_pump.adjust(5)

choice_exp_tank_vol = InlineKeyboardBuilder()
choice_exp_tank_vol.add(
    types.InlineKeyboardButton(text='8', callback_data='8vol'),
    types.InlineKeyboardButton(text='12', callback_data='12vol'),
    types.InlineKeyboardButton(text='35', callback_data='35vol'),
    types.InlineKeyboardButton(text='50', callback_data='50vol'),
    types.InlineKeyboardButton(text='150', callback_data='150vol'),
)
choice_exp_tank_vol.adjust(5)


choice_indirect_boiler_vol = InlineKeyboardBuilder()
choice_indirect_boiler_vol.add(
    types.InlineKeyboardButton(text='80', callback_data='80liters'),
    types.InlineKeyboardButton(text='100', callback_data='100liters'),
    types.InlineKeyboardButton(text='120', callback_data='120liters'),
    types.InlineKeyboardButton(text='140', callback_data='140liters'),
    types.InlineKeyboardButton(text='200', callback_data='200liters'),
    types.InlineKeyboardButton(text='250', callback_data='250liters'),
    types.InlineKeyboardButton(text='300', callback_data='300liters'),
    types.InlineKeyboardButton(text='400', callback_data='400liters'),
    types.InlineKeyboardButton(text='500', callback_data='500liters'),
)
choice_indirect_boiler_vol.adjust(4)










# stena_kotel_price_range = InlineKeyboardBuilder()
# stena_kotel_price_range.add(
#     types.InlineKeyboardButton(text='250 000 - 300 000', callback_data='250000-300000'),
#     types.InlineKeyboardButton(text='300 000 - 400 000', callback_data='300-400')
# )
# stena_kotel_price_range.adjust(1)

# stena_kotel_price_diapozon = InlineKeyboardMarkup(row_width=1)
# stena_price_diap_btn1 = InlineKeyboardButton(text='250 000 - 300 000', callback_data='250t')
# stena_price_diap_btn2 = InlineKeyboardButton(text='300 000 - 400 000', callback_data='300t')





# choice_flue_diametr = InlineKeyboardMarkup(row_width=3)
# flue_diametr_btn1 = InlineKeyboardButton(text='100', callback_data='100d')
# flue_diametr_btn2 = InlineKeyboardButton(text='140', callback_data='140d')
# flue_diametr_btn3 = InlineKeyboardButton(text='150', callback_data='150d')

# water_heater_vol = InlineKeyboardMarkup(row_width=4)
# water_heater_btn1 = InlineKeyboardButton(text='10', callback_data='10lw')
# water_heater_btn2 = InlineKeyboardButton(text='15', callback_data='15lw')
# water_heater_btn3 = InlineKeyboardButton(text='20', callback_data='20lw')
# water_heater_btn4 = InlineKeyboardButton(text='30', callback_data='30lw')
# water_heater_btn5 = InlineKeyboardButton(text='50', callback_data='50lw')
# water_heater_btn6 = InlineKeyboardButton(text='80', callback_data='80lw')
# water_heater_btn7 = InlineKeyboardButton(text='100', callback_data='100lw')

# kos_heater_choice = InlineKeyboardMarkup(row_width=4)
# kos_heater_btn1 = InlineKeyboardButton(text='80', callback_data='80lkb')
# kos_heater_btn2 = InlineKeyboardButton(text='100', callback_data='100lkb')
# kos_heater_btn3 = InlineKeyboardButton(text='120', callback_data='120lkb')
# kos_heater_btn4 = InlineKeyboardButton(text='140', callback_data='140lkb')
# kos_heater_btn5 = InlineKeyboardButton(text='200', callback_data='200lkb')
# kos_heater_btn6 = InlineKeyboardButton(text='300', callback_data='300lkb')
# kos_heater_btn7 = InlineKeyboardButton(text='400', callback_data='400lkb')
# kos_heater_btn8 = InlineKeyboardButton(text='500', callback_data='500lkb')

# pump_view_choice = InlineKeyboardMarkup(row_width=2)
# pump_choice_btn1 = InlineKeyboardButton(text='Циркуляционные насосы', callback_data='circule')
# pump_choice_btn2 = InlineKeyboardButton(text='Дренаж и Насосные станции', callback_data='pump_station')



# floor_kotel_price_diapozon = InlineKeyboardMarkup(row_width=1)
# floor_price_btn1 = InlineKeyboardButton(text='', callback_data='')
# floor_price_btn1 = InlineKeyboardButton(text='', callback_data='')


# main_menu.add(catalog_btn)
# catalog_menu.add(stena_kotels_btn, pol_kotels_btn, dimohod_btn, water_heater_btn, circ_pump_btn, heating_floor_btn, exp_tank_btn, station_pump_btn, drinage_pump_btn, indirect_boiler_btn)
# choice_stena_kotel_power.add(power_kotel_btn1, power_kotel_btn2, power_kotel_btn3, power_kotel_btn4, power_kotel_btn5, power_kotel_btn6, power_kotel_btn7, power_kotel_btn8, power_kotel_btn9, power_kotel_btn10, power_kotel_btn11)
# choice_floor_kotels_power.add(power_floor_btn1, power_floor_btn2, power_floor_btn3, power_floor_btn4, power_floor_btn5, power_floor_btn6, power_floor_btn7, power_floor_btn8, power_floor_btn9, power_floor_btn10)
# choice_flue_diametr.add(flue_diametr_btn1, flue_diametr_btn2, flue_diametr_btn3)
# water_heater_vol.add(water_heater_btn1, water_heater_btn2, water_heater_btn3, water_heater_btn4, water_heater_btn5, water_heater_btn6, water_heater_btn7)
# kos_heater_choice.add(kos_heater_btn1, kos_heater_btn2, kos_heater_btn3, kos_heater_btn4, kos_heater_btn5, kos_heater_btn6, kos_heater_btn7, kos_heater_btn8)
# pump_view_choice.add(pump_choice_btn1, pump_choice_btn2)


# stena_kotel_price_diapozon.add(stena_price_diap_btn1, stena_price_diap_btn2)
