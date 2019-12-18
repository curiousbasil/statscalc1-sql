import sqlite3

conn = sqlite3.connect('/web/SQlite-Data/example.db')

c = conn.cursor()

c.execute('''
          CREATE TABLE item
          (name varchar(250) NOT NULL, cost_price INTEGER PRIMARY KEY ASC, selling_price cost_price INTEGER PRIMARY KEY ASC, quantity INTEGER NOT NULL)
          ''')

conn.commit()

conn.close()


