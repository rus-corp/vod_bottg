import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), unique=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Product(Base):
    __tablename__ = 'product'

    id = sq.Column(sq.Integer, primary_key=True)
    power = sq.Column(sq.Float, nullable=False)
    name = sq.Column(sq.String(length=100), unique=True)
    discription = sq.Column(sq.Text, nullable=False)
    price = sq.Column(sq.Integer, default=0)
    country = sq.Column(sq.String(length=100))
    category_id = sq.Column(sq.Integer, sq.ForeignKey(Category.id), nullable=False)


    category = relationship(Category, backref='products')

    def __str__(self) -> str:
        return f'{self.name}-{self.power}-{self.price}'


class Client(Base):
    __tablename__ = 'client'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String, default=None)
    surname = sq.Column(sq.String, default=None)
    phone = sq.Column(sq.Text, nullable=False)

    def __str__(self) -> str:
        return f'{self.name}-{self.phone}'


class CLientAdres(Base):
    __tablename__ = 'adres'

    id = sq.Column(sq.Integer, primary_key=True)
    city = sq.Column(sq.String, nullable=False)
    street = sq.Column(sq.Text, nullable=False)
    house = sq.Column(sq.Text, nullable=False)
    flat = sq.Column(sq.Integer, nullable=False)
    client_id = sq.Column(sq.Integer, sq.ForeignKey(Client.id), nullable=False)
    
    client = relationship(Client, backref='adress')

    def __str__(self) -> str:
        return f'{self.client}{self.street}, {self.house}-{self.flat}'


class Order(Base):
    __tablename__ = 'order'

    id = sq.Column(sq.Integer, primary_key=True)

    def __str__(self) -> str:
        return f'{self.id}-{self.product}:{self.count}'


class OrderProduct(Base):
    __tablename__ = 'order_product'

    __table_args__ = (sq.PrimaryKeyConstraint('order_id', 'product_id'),)

    order_id = sq.Column(sq.Integer, sq.ForeignKey('order.id'))
    product_id = sq.Column(sq.Integer, sq.ForeignKey('product.id'))

    count = sq.Column(sq.Integer, default=1)


class OrderClient(Base):
    __tablename__ = 'order_client'

    __table_args__ = (sq.PrimaryKeyConstraint('order_id', 'client_id'),)

    order_id = sq.Column(sq.Integer, sq.ForeignKey('order.id'))
    client_id = sq.Column(sq.Integer, sq.ForeignKey('client.id'))



# def create_table(engine):
#     Base.metadata.drop_all(engine)    
#     Base.metadata.create_all(engine)



