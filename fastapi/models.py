from sqlmodel import SQLModel, Field
from typing import Optional


class media(SQLModel, table=True):
    bibnum: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    publisher: str
    isbn: str
    publicationyear: str
    subjects: str
    itemtype: str
    itemcount: int
