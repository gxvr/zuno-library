from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.index import book 

app = FastAPI()

# Enable API Access
origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book)