from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import sqlite3
import sqlalchemy as db
import os

db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'testsqllite.db')
print(db_path)
engine = db.create_engine(f'sqlite:///{db_path}')
connection = engine.connect()
metadata = db.MetaData()
users = db.Table('Users', metadata, autoload=True, autoload_with=engine)

class User(BaseModel):
    name: str
    email: str = None

app = FastAPI()

@app.get("/user/{name}")
async def get_user_by_name(name:str):
    user = get_user(name)
    return JSONResponse(content=jsonable_encoder(user))

def get_user(name):
    query = db.select([users.columns.name, users.columns.email]).where(users.columns.name == name)
    resultproxy = connection.execute(query)
    resultset = resultproxy.fetchall()
    user = User(
        name = resultset[0].name,
        email = resultset[0].email
    )
    return user