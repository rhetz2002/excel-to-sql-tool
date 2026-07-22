import sqlite3 as sq

database = sq.connect(input('enter '))

# initiates coursor as db

db = database.cursor()

# executes SQL here to create the data tables

# im sure that theres a way to create
# the table depending on the contents
# of the xlsx file but for the puroposes
# of the asignment ill just hard code it
                

# creates table that wont work with the givin sceema in db

db.execute(""" CREATE TABLE test1 (
               dummy int PRIMARY KEY NOT NULL,
               dummy_dummy text NOT NULL,
               employ text NOT NULL,
               dep text,
               stttt real)""")
