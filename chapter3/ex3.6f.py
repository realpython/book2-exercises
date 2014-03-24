# hw3.6b.py - JOINing data from multiple tables

"""Rewrite the previous examples using the correct syntax:

SELECT orders.orderid, clients.name, orders.date 
FROM orders INNER JOIN clients ON orders.clientid = clients.clientid;

Verify that your results are correct by comparing them to the previous examples' results."""


import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT DISTINCT population.city, population.population,
                regions.region FROM population INNER JOIN regions WHERE
                population.city = regions.city ORDER by population.city ASC""")

    rows = c.fetchall()

    for r in rows:
        print "City: " + r[0]
        print "Population: " + str(r[1])
        print "Region: " + r[2]
        print



