# db_migrate.py
   
   
from views import db
from datetime import datetime
from config import DATABASE_PATH
import sqlite3
    
with sqlite3.connect(DATABASE_PATH) as connection:
    
    # get a cursor object used to execute SQL commands
    c = connection.cursor()
    
    # temporarily change the name of ftasks table
    c.execute("""ALTER TABLE ftasks RENAME TO old_ftasks""")
    
    # recreate a new ftasks table with updated schema
    db.create_all()
    
    # retrieve data from old_ftasks table
    c.execute("""SELECT name, due_date, priority,
                status FROM old_ftasks ORDER BY task_id ASC""")
    
    # save all rows as a list of tuples; set posted_date to now and user_id to 1
    data = [(row[0], row[1], row[2], row[3],
                datetime.now(), 1) for row in c.fetchall()]
    
    # insert data to ftasks table
    c.executemany("""INSERT INTO ftasks (name, due_date, priority, status,
                    posted_date, user_id) VALUES (?, ?, ?, ?, ?, ?)""", data)
    
    # delete old_ftasks table
    c.execute("DROP TABLE old_ftasks")
