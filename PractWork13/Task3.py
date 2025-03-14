import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute("UPDATE users SET age = 31 WHERE name = 'Alice'")

cursor.execute("DELETE FROM users WHERE name = 'Bob'")

conn.commit()
conn.close()
