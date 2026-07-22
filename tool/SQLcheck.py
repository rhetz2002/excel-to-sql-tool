import time
import sqlite3 as sq


# defines SQL_check function
def SQL_check(filepath):

    log = ''

    # var for while loop
    # while loop will not end until sql
    # file is present and db_open is set to true

    db_open = False

    # while loop while var is false indicating there is no sql file
    # the loop will continue, will end when var is set to true
    # indicating sql file is present

    while db_open is False:

        # tries to open file in file path

        try:

            # attempts to open file, purposefully made
            # to fail if its not there as a QoL feature
            # as a measure to make sure the user knows that
            # its not typed in correctly, opens if already exists

            database = sq.connect(f"file:{filepath}?mode=rw", uri=True)

            log = log + f'{time.strftime("%I:%M:%S %p")}: opened {filepath}\n'

            db = database.cursor()

            # checks selected db file's schema to check if it matches

            db.execute('SELECT employee_ID FROM employee_sales')
            db.execute('SELECT employee_name FROM employee_sales')
            db.execute('SELECT employee_email FROM employee_sales')
            db.execute('SELECT department FROM employee_sales')
            db.execute('SELECT sales FROM employee_sales')

            # sets db_open to true to end loop

            db_open = True

        except:

            # if oppening fails

            try:

                database = sq.connect(f"file:{filepath}?mode=rw", uri=True)

                if input("there is a database here but the schema required "
                         "dose not exist, do you want"
                         " to add it? [Y/N] ").lower() == 'y':

                    log = log + f'{time.strftime("%I:%M:%S %p")}: required ' \
                                f'db schema not found in {filepath}, asking' \
                                f' user for permission to create schema\n'

                    db = database.cursor()

                    # creates table in db

                    log += 'attempting to create new '
                    log += 'table in existing db file\n'

                    db.execute(
                                """ CREATE TABLE IF NOT EXISTS employee_sales (
                                employee_ID int PRIMARY KEY NOT NULL,
                                employee_name text NOT NULL,
                                employee_email text NOT NULL,
                                department text,
                                sales real)""")

                    database.commit()

                    db.execute("PRAGMA table_info(employee_sales)")
                    column_name = [column[1] for column in db.fetchall()]

                    if 'employee_name' not in column_name:

                        try:

                            db.execute(
                                'ALTER TABLE employee_sales '
                                'ADD employee_name text NOT NULL')

                            database.commit()

                        except:

                            log += 'appending to existing schema:'
                            log += ' failed to create employee_name\n'

                    if 'employee_email' not in column_name:

                        try:

                            db.execute(
                                'ALTER TABLE employee_sales '
                                'ADD employee_email text NOT NULL')

                            database.commit()

                        except:

                            log += 'appending to existing schema: '
                            log += 'failed to create employee_email\n'

                    if 'department' not in column_name:

                        try:

                            db.execute(
                                'ALTER TABLE employee_sales '
                                'ADD department text')

                            database.commit()

                        except:

                            log += 'appending to existing schema: '
                            log += 'failed to create department\n'

                    if 'sales' not in column_name:

                        try:

                            db.execute(
                                'ALTER TABLE employee_sales ADD sales real')

                            database.commit()

                        except:

                            log += 'appending to existing schema:'
                            log += ' failed to create sales\n'

                    log = log + f'{time.strftime("%I:%M:%S %p")}: ' \
                                f'successfully ' \
                                f'added database schema in {filepath}\n'

                    # sets db to true

                    db_open = True

            except:

                if input('there is no valid database file in this location '
                         'do you want to create one?[Y/N]: ').lower() == 'y':

                    # creates file

                    log += f'{time.strftime("%I:%M:%S %p")}: created ' \
                       f'new database file in {filepath}\n'

                    # creates db from input file path

                    database = sq.connect(filepath)

                    # initiates cursor as db

                    db = database.cursor()

                    # executes SQL here to create the data tables

                    log = log + f'{time.strftime("%I:%M:%S %p")}: ' \
                                f'successfully ' \
                                f'created database in {filepath}\n'

                    # creates table in db

                    db.execute(""" CREATE TABLE employee_sales (
                               employee_ID int PRIMARY KEY NOT NULL,
                               employee_name text NOT NULL,
                               employee_email text NOT NULL,
                               department text,
                               sales real)""")

                    # sets db to true

                    db_open = True

        finally:

            if not db_open:

                # if user selects no in last prompt,
                # prompts user to input path to SQL file again

                filepath = input('input path to database file,'
                                 ' include file name and extension: ')

    # commits the changes made if any then closes

    database.commit()
    database.close()

    # returns clean

    return log, filepath
