# import sqlite3
#
# conn = sqlite3.connect("new.db")
#
# cursor = conn.cursor()

# cursor.execute("""CREATE TABLE population
#                 (city TEXT, state TEXT, population INT)
#                 """)
#
# cursor.execute("INSERT INTO population VALUES('New York City', \
#     'NY', 8200000)")
# cursor.execute("INSERT INTO population VALUES('San Francisco', \
#     'SF', 800000)")


# conn.commit()
#
# conn.close()


# import sqlite3
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#     c.execute("INSERT INTO population VALUES('New York City', \
#     'NY', 8200000)")
#     c.execute("INSERT INTO population VALUES('San Francisco', \
#     'CA', 800000)")


# import sqlite3
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#
#     # insert multiple records using a tuple
#     cities = [
#             ('Boston', 'MA', 600000),
#             ('Chicago', 'IL', 2700000),
#             ('Houston', 'TX', 2100000),
#             ('Phoenix', 'AZ', 1500000)
#              ]
#
#     # insert data into table
#     c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)


# import from CSV

# import the csv library
# import csv
#
# import sqlite3
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#
#     # open the csv file and assign it to a variable
#     employees = csv.reader(open("employees.csv", "rU"))
#
#     # create a new table called employees
#     c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
#
#     # insert data into table
#     c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)


# INSERT Command with Error Handler


# import the sqlite3 library
# import sqlite3
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#     rows = c.execute("SELECT firstname, lastname FROM employees")
#     for r in rows.fetchall():
#         print(r)



# try:
#         # insert data
#         c.execute("INSERT INTO population VALUES('New York City', 'NY', 8400000)")
#         c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")
#
# except sqlite3.OperationalError as err:
#     print("Oops!  Something went wrong. Try again...", err)
#
# # close the database connection
#
# import sqlite3
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#
#     # update data
#     c.execute("UPDATE population SET population = 9000000 WHERE city='New York City'")
#
#     # delete data
#     c.execute("DELETE FROM population WHERE city='Boston'")
#
#     print("\nNEW DATA:\n")
#
#     c.execute("SELECT * FROM population")
#
#     rows = c.fetchall()
#
#     for r in rows:
#         print(r[0], r[1], r[2])


# import sqlite3
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#
#     # insert multiple records using a tuple
#     # (you can copy and paste the values)
#     cities = [
#                 ('Boston', 'MA', 600000),
#                 ('Los Angeles', 'CA', 38000000),
#                 ('Houston', 'TX', 2100000),
#                 ('Philadelphia', 'PA', 1500000),
#                 ('San Antonio', 'TX', 1400000),
#                 ('San Diego', 'CA', 130000),
#                 ('Dallas', 'TX', 1200000),
#                 ('San Jose', 'CA', 900000),
#                 ('Jacksonville', 'FL', 800000),
#                 ('Indianapolis', 'IN', 800000),
#                 ('Austin', 'TX', 800000),
#                 ('Detroit', 'MI', 700000)
#             ]
#
#     c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)
#
#     c.execute("SELECT * FROM population WHERE population > 1000000")
#
#     rows = c.fetchall()
#
#     for r in rows:
#         print(r[0], r[1], r[2])


#
# import sqlite3
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#     c.execute("""DROP TABLE IF EXISTS regions""")
#     c.execute("""CREATE TABLE regions
#               (city TEXT, region TEXT)
#                """)
#
#     # (again, copy and paste the values if you'd like)
#     cities = [
#             ('New York City', 'Northeast'),
#             ('San Francisco', 'West'),
#             ('Chicago', 'Midwest'),
#             ('Houston', 'South'),
#             ('Phoenix', 'West'),
#             ('Boston', 'Northeast'),
#             ('Los Angeles', 'West'),
#             ('Houston', 'other'),
#             ('Philadelphia', 'Northeast'),
#             ('San Antonio', 'South'),
#             ('San Diego', 'West'),
#             ('Dallas', 'South'),
#             ('San Jose', 'West'),
#             ('Jacksonville', 'South'),
#             ('Indianapolis', 'Midwest'),
#             ('Austin', 'South'),
#             ('Detroit', 'Midwest')
#              ]
#
#     c.executemany("INSERT INTO regions VALUES(?, ? )", cities)
#
#     c.execute("SELECT * FROM regions ORDER BY region ASC")
#
#     rows = c.fetchall()
#
#     for r in rows:
#         print(r[0], r[1])

# import sqlite3
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#
#     # retrieve data
#     c.execute("""SELECT population.city, population.population,
#             regions.region FROM population, regions
#             WHERE population.city = regions.city""")
#
#     rows = c.fetchall()
#
#     for r in rows:
#         print(r[0], r[1], r[2])

# import sqlite3
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#
#     c.execute("""SELECT DISTINCT population.city, population.population,
#                 regions.region FROM population, regions WHERE
#                 population.city = regions.city ORDER by population.city ASC""")
#
#     rows = c.fetchall()
#
#     for r in rows:
#         print("City: " + r[0])
#         print("Population: " + str(r[1]))
#         print("Region: " + r[2])
#         print("")



# - Add another table to accompany your "inventory" table called "orders". This table should have the following fields: "make", "model", and "order_date". Make sure to only include makes and models for the cars found in the inventory table. Add 15 records (3 for each car), each with a separate order date (YYYY-MM-DD).

# import sqlite3
#
# with sqlite3.connect('new.db') as connection:
#     c = connection.cursor()
#     # c.execute("""CREATE TABLE inventory
#     #             (make TEXT, model TEXT, quantity INT)""")
#
#
#     cars = [
#         ('Honda', 'Civic', 100),
#         ('Honda', 'Accord', 150),
#         ('Ford', 'Focus', 200),
#         ('Ford', 'Avenger', 200),
#         ('Ford', 'Ranger', 500),
#     ]
#     c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", cars)
#
#     # orders = [
#     #         ('Ford', 'Focus', '2014-01-22'),
#     #         ('Ford', 'Focus', '2014-01-23'),
#     #         ('Ford', 'Focus', '2014-01-24'),
#     #         ('Honda', 'Civic', '2014-01-25'),
#     #         ('Honda', 'Civic', '2014-01-26'),
#     #         ('Honda', 'Civic', '2014-01-27'),
#     #         ('Ford', 'Ranger', '2014-01-28'),
#     #         ('Ford', 'Ranger', '2014-01-22'),
#     #         ('Ford', 'Ranger', '2014-01-23'),
#     #         ('Honda', 'Accord', '2014-01-24'),
#     #         ('Honda', 'Accord', '2014-01-25'),
#     #         ('Honda', 'Accord', '2014-01-26'),
#     #         ('Ford', 'Avenger', '2014-01-27'),
#     #         ('Ford', 'Avenger', '2014-01-28'),
#     #         ('Ford', 'Avenger', '2014-01-22'),
#     #          ]
#     # c.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)
#     #
#     # for r in c.execute("SELECT * FROM orders"):
#     #     print(r)
#
# # - Finally output the car's make and model on one line, the quantity on another line, and then the order_dates on subsequent lines below that.
#
#
#     for r in c.execute("""SELECT inventory.make, inventory.model, inventory.quantity, orders.order_date
#                 FROM inventory
#                 JOIN orders
#                 ON inventory.model = orders.model
#                 """):
#         print(r[0], r[1])
#         print(r[2])
#         print(r[3])
#         print('---------------')
#
#
# import sqlite3
#
# with sqlite3.connect("new.db") as connection:
#     c = connection.cursor()
#
#     # # create a dictionary of sql queries
#     # sql = {'average': "SELECT avg(population) FROM population",
#     #        'maximum': "SELECT max(population) FROM population",
#     #        'minimum': "SELECT min(population) FROM population",
#     #        'sum': "SELECT sum(population) FROM population",
#     #        'count': "SELECT count(city) FROM population"}
#     #
#     # # run each sql query item in the dictionary
#     # for keys, values in sql.items():
#     #
#     #     # run sql
#     #     c.execute(values)
#     #
#     #     # fetchone() retrieves one record from the query
#     #     result = c.fetchOne()
#     #
#     #     # output the result to screen
#     #     print(keys + ":", result[0])
#     #
#     result = c.execute("SELECT * FROM inventory")
#     print('Total Quantity: ',result.fetchall())
#
# import sqlite3
# import random
#
# with sqlite3.connect("newnum.db") as connection:
#     c = connection.cursor()
#
#     # delete database table if exist
#     c.execute("DROP TABLE if exists numbers")
#
#     # create database table
#     c.execute("CREATE TABLE numbers(num int)")
#
#     # insert each number to the database
#     for i in range(100):
#         c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))
#
#     rows = c.execute("SELECT * FROM numbers")
#
#     for r in rows:
#         print(r)

import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # delete database table if exist
    c.execute("DROP TABLE if exists numbers")

    # create database table
    c.execute("CREATE TABLE numbers(num int)")

    # insert each number to the database
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))


    prompt = """
    Select the operation that you want to perform [1-5]:
    1. Average
    2. Max
    3. Min
    4. Sum
    5. Exit
    """

    # loop until user enters a valid operation number [1-5]
    while True:
        # get user input
        x = input(prompt)

        # if user enters any choice from 1-4
        if x in set(["1", "2", "3", "4"]):
            # parse the corresponding operation text
            operation = {1: "avg", 2:"max", 3:"min", 4:"sum"}[int(x)]
            print(operation)
            # retrieve data
            c.execute("SELECT {}(num) from numbers".format(operation))

            # fetchone() retrieves one record from the query
            get = c.fetchone()

            # output result to screen
            print(operation + ":  %f" % get[0])

        # if user enters 5
        elif x == "5":
            print("Exit")

            # exit loop
            break
