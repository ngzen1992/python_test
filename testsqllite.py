import sqlite3

con = sqlite3.connect('testsqllite.db')
cur = con.cursor()

### Insert a row of data
# cur.execute("INSERT INTO Users VALUES ('Jesslyn Low', 'smlow@gmail.com')")
# print('One user added')

### Read all from Users
# for row in cur.execute("SELECT * FROM Users WHERE Name = 'Zen'") :
#     print(row)

name = 'Zen'
cur.execute(f"SELECT rowid, name, email FROM Users WHERE Name = '{name}'")
row = cur.fetchone()
print(f'id: {row[0]} name: {row[1]} email: {row[2]}')

# con.commit()

con.close()