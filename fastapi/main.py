from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from models import media
from database import engine
from sqlmodel import Session, select
from typing import Optional, List


app = FastAPI()

session = Session(bind=engine)


@app.get('/books', response_model=List[media],
         status_code=status.HTTP_200_OK)
async def get_all_books():
    statement = select(media)
    results = session.exec(statement).all()

    return results


@app.get('/books/{bibnum}', response_model=media)
async def get_a_book(bibnum: int):
    statement = select(media).where(media.bibnum == bibnum)

    result = session.exec(statement).first()

    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return result
