# Create a SQLite3 database and table


import sqlite3

with sqlite3.connect("movies.db") as connection:
    c = connection.cursor()

    # create a table
    c.execute("""CREATE TABLE new_movies
                        (title TEXT, year INT, votes text,
                        release_date text, rating INT, metascore INT)""")
