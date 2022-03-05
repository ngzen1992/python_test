import sqlite3

con = sqlite3.connect('testsqllite.db')
cur = con.cursor()

### Insert a row of data
# cur.execute("INSERT INTO Users VALUES ('Jesslyn Low', 'smlow@gmail.com')")
# print('One user added')

### Read all from Users
# for row in cur.execute('SELECT * FROM Users') :
#     print(row)

cur.execute('SELECT * FROM Users')
print(cur.fetchone())

con.commit()

con.close()