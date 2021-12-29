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
    Column('itemtype', String(100),ForeignKey('media_type.code')),
    Column('itemcount', Integer)
)

mediatype = Table(
    'media_type', meta,
    Column('code', String(100), primary_key=True),
    Column('description', String(255)),
    Column('code type', String(100)),
    Column('format group', String(100)),
    Column('format subgroup', String(100)),
    Column('category group', String(100)),
    Column('category subgroup', String(100)),
)
