# Create a SQLite3 database and table


import sqlite3

with sqlite3.connect("movies.db") as connection:
    c = connection.cursor()

    # create a table
    c.execute("""CREATE TABLE new_movies
                        (title TEXT, year INT, rating text,
                        release text, runtime INT, critics_review INT,
                        audience_review INT)""")
