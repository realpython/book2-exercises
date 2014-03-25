# GET data from Rotten Tomatoes, parse, and write to database


import json
import requests
import sqlite3

YOUR_OWN_KEY = 'GET_YOUR_OWN_KEY'
url = requests.get("http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=%s" %
        (YOUR_OWN_KEY,))

# convert data from feed to binary
binary = url.content

# decode the json feed
output = json.loads(binary)

# grab the list of movies
movies = output["movies"]

with sqlite3.connect("movies.db") as connection:
    c = connection.cursor()

    # iterate through each movie and write to the database
    for movie in movies:
        c.execute("INSERT INTO new_movies VALUES(?, ?, ?, ?, ?, ?, ?)",
                (movie["title"], movie["year"], movie["mpaa_rating"],
                movie["release_dates"]["theater"], movie["runtime"],
                movie["ratings"]["critics_score"],
                movie["ratings"]["audience_score"]))

    # retrieve data
    c.execute("SELECT * FROM new_movies ORDER BY title ASC")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1], r[2], r[3], r[4], r[5], r[6]
