from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://Zuno:ZunoInterview@zunolibrary.cv07g5ggoiyj.us-east-2.rds.amazonaws.com:3306/library")

meta = MetaData()
conn = engine.connect()