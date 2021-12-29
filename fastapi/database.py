from sqlmodel import SQLModel, create_engine
import os

conn_str = "mysql+pymysql://Zuno:ZunoInterview@zunolibrary.cv07g5ggoiyj.us-east-2.rds.amazonaws.com:3306/library"

engine = create_engine(conn_str, echo=True)
