# Assignment 2a - insert random data


# import the sqlite3 library
import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # delete database table if exist
    c.execute("drop table if exists numbers")

    # create database table
    c.execute("CREATE TABLE numbers(num int)")

    # insert each number to the database
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))
