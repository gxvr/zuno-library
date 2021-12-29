from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import media
from models import media_type
from models import checkout_data
from database import engine
from sqlmodel import Session, select
from typing import Optional, List


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

session = Session(bind=engine)


@app.get('/')
def read_root():
    return {"Bond": "James Bond"}


@app.get('/media', response_model=List[media],
         status_code=status.HTTP_200_OK)
async def get_all_books():
    statement = select(media)
    results = session.exec(statement).all()
    return results


@app.get('/media/{bibnum}', response_model=media)
async def get_a_book(bibnum: int):
    statement = select(media).where(media.bibnum == bibnum)
    result = session.exec(statement).first()
    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result


@app.get('/type', response_model=List[media_type],
         status_code=status.HTTP_200_OK)
async def get_media_type():
    statement = select(media_type)
    results = session.exec(statement).all()
    return results


@app.get('/checkout', response_model=List[checkout_data],
         status_code=status.HTTP_200_OK)
async def get_checkout_data():
    statement = select(checkout_data)
    results = session.exec(statement).all()
    return results


@app.get('/books')
def library():
    with Session(engine) as session:
        statement = select(media, media_type, checkout_data).where(
            media.itemtype == media_type.code).where(checkout_data.bibnumber == media.bibnum)
        results = session.exec(statement).all()
        for result in results:
            return results


@app.get('/books/{bibnum}')
def library_book(bibnum: int):
    with Session(engine) as session:
        statement = select(media, media_type).where(
            media.itemtype == media_type.code).where(checkout_data.bibnumber == media.bibnum).where(media.bibnum == bibnum)
        results = session.exec(statement).all()
        return results
