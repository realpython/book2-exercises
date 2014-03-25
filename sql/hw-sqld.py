# WHERE clause

"""Finally output only records that are for Ford vehicles."""


import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * from inventory WHERE make = 'Ford'")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output headers
    print 'Make Model Qty'
    print '--------------'

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1], r[2]
