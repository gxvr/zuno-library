from sqlalchemy import Table, Column, Integer, String, ForeignKey
from config.db import meta

books = Table(
    'media', meta,
    Column('bibnum', Integer, primary_key=True),
    Column('title', String(255)),
    Column('author', String(255)),
    Column('isbn', String(100)),
    Column('publicationyear', String(100)),
    Column('publisher', String(100)),
    Column('subjects', String(255)),
    Column('itemtype', String(100)),
    Column('itemcount', Integer)
)