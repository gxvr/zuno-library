from fastapi import APIRouter
from config.db import conn
from models.index import books
from schemas.index import Book

book = APIRouter()

# Fetch All
@book.get("/")
def read_data():
    return {"msg": "Zuno Library API"}
    
# Fetch All
@book.get("/books")
async def read_data():
    return conn.execute(books.select()).fetchall()


# Fetch by ID
@book.get("/books/{bibnum}")
async def read_data(bibnum: int):
    return conn.execute(books.select().where(books.c.bibnum == bibnum)).fetchall()



