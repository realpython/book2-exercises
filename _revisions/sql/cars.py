import sqlite3

conn = sqlite3.connect('cars.db')

cursor = conn.cursor()

cursor.execute("""create table cars
                (make TEXT, model TEXT, quantity INT)""")

con.close()
