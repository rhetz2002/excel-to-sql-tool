import time
import sqlite3 as sq


# defines vaildate function
def SQL_check(filepath):

    log = ''

    # for while loop
    # while loop will not end untill sql
    # file is present and db_open is set to true

    db_open = False

    # while loop while var is false indicating there is no sql file
    # the loop will continue, will end when var is true
    # indicating sql file is present

    while (db_open is False):
        
        # trys to open file in file path
        

        try:

            # attempts to open file, purposefully made
            # to fail if its not there as a qol feature
            # as a measure to make sure the user knows that
            # its not typed in correctly, opens if alredy exsists
            
            database = sq.connect(f"file:{filepath}?mode=rw", uri=True)

            log = log + f'{time.strftime("%I:%M:%S %p")}: opened {filepath}\n'

            db = database.cursor()
            
            # checks selected db file's schema to check if it matches

            db.execute('SELECT employee_ID FROM employee_sales')   
            db.execute('SELECT employee_name FROM employee_sales')
            db.execute('SELECT employee_email FROM employee_sales')
            db.execute('SELECT department FROM employee_sales')
            db.execute('SELECT sales FROM employee_sales')
                       

            # if not, sets variable in order to have specail error mesage propting 
            # user to re-enter or posibly injecting new table into db  

            # sets db_open to true to end loop

            db_open = True

        except:
            
            
            try: 
            
                database = sq.connect(f"file:{filepath}?mode=rw", uri=True)


                if input ("there is a db here but the schema required dose not exist, do you want to add it? [Y/N] ").lower() == 'y':
                
                    log = log + f'{time.strftime("%I:%M:%S %p")}: required db ' \
                                f'schema not found in {filepath}, asking user for permision to create schema\n'

                    db = database.cursor()
                
                    # creates table in db
                    
                    log += 'atempting to create new table in exsisting db file'

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
                            
                            db.execute('ALTER TABLE employee_sales ADD employee_name text NOT NULL')

                            database.commit()
                        
                        except:
                            
                            log += 'appending to exsisting schema: failed to create employee_name'

                    if 'employee_email' not in column_name:

                        try:
                            
                            db.execute('ALTER TABLE employee_sales ADD employee_email text NOT NULL')

                            database.commit()
                        
                        except:
                            
                            log += 'appending to exsisting schema: failed to create employee_email'

                    if 'department' not in column_name:

                        try:
                            
                            db.execute('ALTER TABLE employee_sales ADD department text')

                            database.commit()
                        
                        except:
                            
                            log += 'appending to exsisting schema: failed to create department'

                    if 'sales' not in column_name:
                        
                        try:
                            
                            db.execute('ALTER TABLE employee_sales ADD sales real')

                            database.commit()
                        
                        except:
                            
                            log += 'appending to exsisting schema: failed to create sales'
                    
                             
                    print (column_name)



                    log = log + f'{time.strftime("%I:%M:%S %p")}: sucseffully ' \
                                f'added database schema in {filepath}\n'
                    
                    # sets db to true

                    db_open = True
                    

            except:

                if input('there is no valid file in this location '
                      'do you want to create one?[Y/N]: ').lower() == 'y':

                    # creates file

                    log += f'{time.strftime("%I:%M:%S %p")}: created ' \
                       f'new database file in {filepath}\n'

                    # creates db from input file path
                
                    database = sq.connect(filepath)

                    # initiates coursor as db

                    db = database.cursor()

                    # executes SQL here to create the data tables

                    # im sure that theres a way to create
                    # the table depending on the contents
                    # of the xlsx file but for the puroposes
                    # of the asignment ill just hard code it
                
                    log = log + f'{time.strftime("%I:%M:%S %p")}: sucseffully ' \
                            f'created database in {filepath}\n'

                    # creates table in db

                    db.execute(
                    """ CREATE TABLE employee_sales (
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
                # prompts user to input path to sql file again

                filepath = input('input path to database file, include file name: ')
            
    database.commit()
    database.close()            
    
    # returns clean

    return log, filepath