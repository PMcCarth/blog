#associated with notes
#creating our sql table and populating it

import sqlite3

#creating the db if it doesn't exist already
with sqlite3.connect("blog.db") as connection:
    #creating a cursor()
    c = connection.cursor()

    #creating the table
    c.execute("""CREATE TABLE posts(title TEXT, post TEXT)""")

    #insert dummy data into the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Ok", "I\'m ok")')

    #notice how we escaped the apostrophes
