import sqlalchemy
from sqlalchemy.orm import sessionmaker
import csv
from .models import Product, Category
import asyncio


import psycopg2
import os
db_log = {"database": "vod_db", "user": "postgres", "password": "2909"}


async def get_wall_kotels(power):
    conn = psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password'])
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name, power, price FROM product
        WHERE power = %s AND category_id = 1""", [power]
        )
        conn.commit()
        data = cur.fetchall()
        return data



async def get_floor_kotels(power):
    conn = psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password'])
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name, power, price FROM product
        WHERE power = %s AND category_id = 2""", [power]
        )
        conn.commit()
        data = cur.fetchall()
        return data

async def get_chimneys():
    conn = psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password'])
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name, power, price FROM product
        WHERE category_id = 3"""
        )
        conn.commit()
        data = cur.fetchall()
        return data

async def get_el_water_heater(power):
    conn = psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password'])
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name, power, price FROM product
        WHERE power = %s AND category_id = 4""", [power]
        )
        conn.commit()
        data = cur.fetchall()
        return data


async def get_circ_pump(power):
    conn = psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password'])
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name, power, price FROM product
        WHERE power = %s AND category_id = 5""", [power]
        )
        conn.commit()
        data = cur.fetchall()
        return data


async def get_exp_tank(power):
    conn = psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password'])
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name, power, price FROM product
        WHERE power = %s AND category_id = 7""", [power]
        )
        conn.commit()
        data = cur.fetchall()
        return data


async def get_pump_station():
    conn = psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password'])
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name, power, price FROM product
        WHERE category_id = 9"""
        )
        conn.commit()
        data = cur.fetchall()
        return data


async def get_indirect_boiler(power):
    conn = psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password'])
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name, power, price FROM product
        WHERE power = %s AND category_id = 10""", [power]
        )
        conn.commit()
        data = cur.fetchall()
        return data


async def get_heat_floor():
    conn = psycopg2.connect(database=db_log['database'], user=db_log['user'], password=db_log['password'])
    with conn.cursor() as cur:
        cur.execute("""
        SELECT name, power, price FROM product
        WHERE category_id = 6"""
        )
        conn.commit()
        data = cur.fetchall()
        return data



# DSN = 'postgresql://postgres:2909@localhost:5432/vod_db'
# engine = sqlalchemy.create_engine(DSN)

# # create_table(engine)

# Session = sessionmaker(bind=engine)
# session = Session()


# cat1 = Category(name='Настенные котлы')
# cat2 = Category(name='Напольные котлы')
# cat3 = Category(name='Дымоходы')
# cat4 = Category(name='Водонагреватели')
# cat5 = Category(name='Циркуляционные насосы')
# cat6 = Category(name='Теплый пол')
# cat7 = Category(name='Расширительные баки')
# cat8 = Category(name='Насосные станции')
# cat9 = Category(name='Дренажные насосы')
# cat10 = Category(name='Косвенные бойлера')

# session.add_all([cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10])
# session.commit()

# with open('data.csv', 'r', encoding='utf-8') as file:
#     product = list(csv.DictReader(file, delimiter=';'))

# for prod in product:
#     pr = Product(name=prod['name'], power=prod['power'], discription=prod['discription'], price=prod['price'], country=prod['country'], category_id=prod['categories_id'])
#     session.add(pr)
#     session.commit()


# def get_kotels():
#     for c in session.query(Product).join(Category).filter(Category.id == 1).filter(Product.price >= 250000).filter(Product.price <= 300000).all():
#         print (type(c))
#         # prod_list = []
#         # prod_list.append(c)
#         # print (prod_list)

# get_kotels()

# for c in session.query(Product).join(Category).filter(Category.id == 4).all():
#     print(c)


# session.close()