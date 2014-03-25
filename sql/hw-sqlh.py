# JOIN + SQLite Functions

"""Output the car's make and model on one line, the quantity on another line, 
and then the order count on the next line. The latter is a bit difficult, 
but please try it first before looking at the code. **Remember: Google-it-first!**"""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("SELECT * FROM inventory")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        # output the car make, model and quantity to screen
        print r[0], r[1], "\n", r[2]

        # retrieve order_date for the current car make and model
        c.execute("SELECT count(order_date) FROM orders WHERE make=? and model=?",
                (r[0], r[1]))

        # fetchone() retrieves one record from the query
        order_count = c.fetchone()[0]

        # output the order count to the screen
        print order_count

