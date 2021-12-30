# Zuno FastAPI + SQLModel
This is a REST API with FastAPI and SQLModel. SQLModel is a library for interacting with SQL databases from Python code, with Python objects. It is designed to be intuitive, easy to use, highly compatible, and robust.



## Starting the server
- Install the requirements 
```
pip install -r requirements.txt
```

- Add your Mysql database credentials on database.py
```
conn_str = "mysql+pymysql://username:password@host/database"
```

- Finally run the project on port 5051
```
uvicorn main:app --reload --port 5051
```

