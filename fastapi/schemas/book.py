from pydantic import BaseModel

class Book(BaseModel):
    bibnum: int
    title: str
    author: str
    isbn: str
    publicationyear: str
    publisher: str
    subjects: str
    itemtype: str
    itemcount: int