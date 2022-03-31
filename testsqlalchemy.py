import sqlalchemy as db
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'testsqllite.db')
print(db_path)
engine = db.create_engine(f'sqlite:///{db_path}')
connection = engine.connect()
metadata = db.MetaData()
users = db.Table('Users', metadata, autoload=True, autoload_with=engine)

query = db.select([users.columns.id, users.columns.name, users.columns.email])
resultproxy = connection.execute(query)
resultset = resultproxy.fetchall()
print(resultset[0].rowid)
