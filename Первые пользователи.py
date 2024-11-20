import sqlite3


conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)', users)

cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')

cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age!=60')

results = cursor.fetchall()

for x in results:
    username, email, age, balance = x
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

cursor.execute('DELETE FROM users WHERE id = 6')

cursor.execute('SELECT COUNT (*) FROM users')
one = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM users')
two = cursor.fetchone()[0]

if one > 0:
    cr = two/one
else:
    cr = 0
print(cr)

conn.commit()
conn.close()