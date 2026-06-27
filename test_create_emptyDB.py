import sqlite3 as sq

database = sq.connect("tool/output/empty.db")

db = database.cursor()

db.execute(
                    """ CREATE TABLE employee_sales (                                           
                        employee_ID int PRIMARY KEY NOT NULL,
                        employee_name text NOT NULL,
                        employee_email text NOT NULL,
                        department text,
                        sales real)""")         