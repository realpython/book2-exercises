# JOINing data from multiple tables

"""Finally output the car's make and model on one line, 
the quantity on another line, and then the order_dates on subsequent lines below that."""


import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""SELECT inventory.make, inventory.model,
            inventory.quantity, orders.order_date FROM inventory INNER JOIN orders
            ON inventory.model = orders.model""")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
        print r[2]
        print r[3]
        print
