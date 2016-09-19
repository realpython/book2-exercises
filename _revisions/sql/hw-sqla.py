# Create a SQLite3 database and table

"""Create a new database called "cars", and add a table called "inventory" 
that includes the following fields: "Make", "Model", and "Quantity". 
Don't forget to include the proper data-types."""


# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist 
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE inventory
                (make TEXT, model TEXT, quantity INT) 
                """)
                
# close the database connection
conn.close()
