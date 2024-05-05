from xmlrpc.client import Boolean, DateTime
from sqlalchemy import Table,Column, Integer, String, Boolean, DateTime
from .db import meta,engine

orders = Table("orders", meta, 
    Column('id', Integer, primary_key=True),
    Column('client', String(255)),
    Column('sku', String(255)),
    Column('quantity', Integer),
    Column('unit', String(255)),
    Column('time', DateTime),
    Column('state', Boolean, unique=False, default=True)
    )

meta.create_all(engine)