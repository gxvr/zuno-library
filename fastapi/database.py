from sqlmodel import SQLModel, create_engine
import os

conn_str = "mysql+pymysql://username:password@host/database"

engine = create_engine(conn_str, echo=True)
