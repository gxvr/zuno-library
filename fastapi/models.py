from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey
from sqlmodel import SQLModel, Field
from typing import Optional


class media(SQLModel, table=True):
    bibnum: Optional[int] = Field(
        default=None, primary_key=True)
    title: str
    author: str
    publisher: str
    isbn: str
    publicationyear: str
    subjects: str
    itemtype: Optional[str] = Field(
        default=None, foreign_key="media_type.code")
    itemcount: int


class media_type(SQLModel, table=True):
    code: Optional[str] = Field(default=None, primary_key=True)
    description: str
    codetype: str
    formatgroup: str
    formatsubgroup: str
    categorygroup: str
    categorysubgroup: str


class checkout_data(SQLModel, table=True):
    bibnumber: Optional[str] = Field(
        default=None, primary_key=True, foreign_key="media.bibnum")
    itembarcode: int
    itemtype: str
    callnumber: str
    checkoutdatetime: str
