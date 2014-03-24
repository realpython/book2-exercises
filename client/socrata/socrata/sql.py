import sqlite3

conn = sqlite3.connect("project.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE data
        (text TEXT, url TEXT, views TEXT) 
        """)
