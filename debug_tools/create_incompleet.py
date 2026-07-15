import sqlite3 as sq

database = sq.connect(input('enter '))

# initiates coursor as db

db = database.cursor()

# executes SQL here to create the data tables

# im sure that theres a way to create
# the table depending on the contents
# of the xlsx file but for the puroposes
# of the asignment ill just hard code it
                

# creates table in db

db.execute(""" CREATE TABLE employee_sales (
               employee_ID int PRIMARY KEY NOT NULL,
               employee_name text NOT NULL,
               sales real)""")
