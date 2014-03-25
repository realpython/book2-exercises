# INSERT Command

"""Using the "inventory" table from the homework in Lesson 2.2, 
add (`INSERT`) 5 records (rows of data) to the table. 
Make sure 3 of the vehicles are Fords while the other 2 are Hondas. 
Use any model and quantity for each."""

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("cars.db") 

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Focus', 10)")
cursor.execute("INSERT INTO inventory VALUES('Honda', 'Civic', 11)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Ranger', 12)")
cursor.execute("INSERT INTO inventory VALUES('Honda', 'Accord', 13)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Avenger', 14)")

# commit the changes
conn.commit()

# close the database connection
conn.close()
