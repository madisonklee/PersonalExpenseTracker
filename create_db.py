import sqlite3

# establish connection
conn=sqlite3.connect("expenses.db")

# make cursor
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY,
Date DATE,
description TEXT,
category TExT,
price REAL)""")

conn.commit()   # to commit changes
conn.close()