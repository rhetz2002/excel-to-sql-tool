#imports required lib
import sqlite3 as sq
import time


#grabs variables from main.py

# defines output function

def prossess (data):
    
    # initiates log variable

    log = ''

    # for while loop
    # while loop will not end untill sql 
    # file is present and db_open is set to true

    db_open = False

    # user inputs path to file if no file exists one will be created

    file_path = input ('input path to database file, include file name: ')

    # while loop while var is false indicating there is no sql file 
    # the loop will continue, will end when var is true indicating sql file is present

    while (db_open == False):
        
        # trys to open file in file path

        try: 
            
            # stores data from data variable

            data_store = []

            # attempts to open file, purposefully made to fail if its not there as a qol feature   
            # as a measure to make sure the user knows that its not typed in correctly, opens if alredy exsists
            database = sq.connect(f"file:{file_path}?mode=rw", uri=True)

            # if sucseeds initates cursor as db
            
            log = log + f'{time.strftime("%I:%M:%S %p")}: opened {input}\n'

            db = database.cursor()
            
            # iterates over the data in data    

            for index, row in data.iterrows():
                
                # reads row by row adds to data_store

                data_store.append(data.at[index, 'ID'])
                
                data_store.append(data.at[index,'name'])
            
                data_store.append(data.at[index, 'email'])

                data_store.append(data.at[index, 'department'])

                data_store.append(float(data.at[index, 'sales']))
                
                # executes SQL adding the data_store data into the SQL

                db.execute("""
                        INSERT INTO employee_sales 
                        (employee_ID, employee_name, employee_email, department, sales) 
                        VALUES (?, ?, ?, ?, ?)""" ,
                (data_store[0], data_store[1], data_store[2], data_store[3], data_store[4]))           
                
                # resets data_store

                data_store = []

            log = log + f'{time.strftime("%I:%M:%S %p")}: sucseffully inserted data from xlsx to {input}\n'            
            
            # commits and closes database

            database.commit()
            db.close()
            
            # if sucsesffully opens file sets db_open to true to end the loop

            db_open = True

        except: 
            
            # if opening fails asks user if they want to create file

            if input ('there is no file in this location do you want to create one?[Y/N]: ').lower() == 'y' :

                #creates file
                
                f'{time.strftime("%I:%M:%S %p")}: created new database file in {input}\n'

                database = sq.connect(file_path)
                
                # initiates coursor as db

                db = database.cursor()

                # executes SQL here to create the data tables

                # im sure that theres a way to create the table depending on the contents 
                # of the slxs file but for the puroposes of the asignment ill just hard code it 

                db.execute(
                    """ CREATE TABLE employee_sales (                                           
                        employee_ID int PRIMARY KEY NOT NULL,
                        employee_name text NOT NULL,
                        employee_email text NOT NULL,
                        department text,
                        sales real)""")                                                          

                #parses the data and saves in a list which is apended to the database

                for index, row in data.iterrows():
                
                    # reads row by row adds to data_store

                    data_store.append(data.at[index, 'ID'])
                
                    data_store.append(data.at[index,'name'])
            
                    data_store.append(data.at[index, 'email'])

                    data_store.append(data.at[index, 'department'])

                    data_store.append(float(data.at[index, 'sales']))

                    # executes SQL adding the data_store data into the SQL

                    db.execute("""
                        INSERT INTO employee_sales 
                        (employee_ID, employee_name, employee_email, department, sales) 
                        VALUES (?, ?, ?, ?, ?)""",
                    (data_store[0], data_store[1], data_store[2], data_store[3], data_store[4]))           
                
                    # resets data_store

                    data_store = []

                log = log + f'{time.strftime("%I:%M:%S %p")}: sucseffully inserted data from xlsx to {input}\n'

                # commits and closes database

                database.commit()
                
                db.close()
                
                # if sucsesffully opens file sets db_open to true to close the loop
                
                db_open = True

            else: 
                
                # if user selects no in last prompt, prompts user to input path to sql file again 

                file_path = input ('input path to database file, include file name: ')



