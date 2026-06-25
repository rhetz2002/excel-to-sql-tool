#imports required lib
import sqlite3 as sq


#grabs variables from main.py

# defines output function

def out (data):
    
    # for while loop
    # while loop will not end untill sql 
    # file is present and is set to true

    db_open = False

    # user inputs path to file if no file exists one will be created

    file_path = input ('input path to file, include file name: ')

    # while loop while var is false indicating there is no sql file 
    # the loop will continue, will end when var is true indicating sql file is present

    while (db_open == False):
        
        # trys to open file in file path

        try: 
            
            # stores data from data

            data_store = []

            # atempts to open file, purpoussfully made to fail if its not there as a qol feature 
            # as a mesure to make sure the user knows that its not typed in corectly if fails and alredy exsists

            database = sq.connect(f"file:{file_path}?mode=rw", uri=True)

            # if sucseeds initates cursor as db
            
            db = database.cursor()
            
            # iterates over the data in data    

            for index, row in data.iterrows():
                
                data_store.append(data.at[index, 'ID'])
                
                data_store.append(data.at[index,'name'])
            
                data_store.append(data.at[index, 'email'])

                data_store.append(data.at[index, 'department'])

                data_store.append(float(data.at[index, 'sales']))
                
                db.execute("""
                        INSERT INTO employee_sales 
                        (employee_ID, employee_name, employee_email, department, sales) 
                        VALUES (?, ?, ?, ?, ?)""" ,
                (data_store[0], data_store[1], data_store[2], data_store[3], data_store[4]))           
                
                data_store = []

            # will import the sql data to the db here

            for row in db.execute("SELECT * FROM employee_sales"):
                print(row)

            database.commit()
            db.close()
            # if sucsesffully opens file sets db_open to true

            db_open = True

        except: 
            
            # if opening fails asks user if they want to create file

            if input ('there is no file in this location do you want to create one?[Y/N]: ').lower() == 'y' :

                #creates file
                database = sq.connect(file_path)

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
                
                    data_store.append(data.at[index, 'ID'])
                
                    data_store.append(data.at[index,'name'])
            
                    data_store.append(data.at[index, 'email'])

                    data_store.append(data.at[index, 'department'])

                    data_store.append(float(data.at[index, 'sales']))
                
                    db.execute("""
                        INSERT INTO employee_sales 
                        (employee_ID, employee_name, employee_email, department, sales) 
                        VALUES (?, ?, ?, ?, ?)""",
                    (data_store[0], data_store[1], data_store[2], data_store[3], data_store[4]))           
                
                    data_store = []

                # will import the sql data to the db here
                
                for row in db.execute("SELECT * FROM employee_sales"):
                    print(row)

                database.commit()
                
                db.close()
                
                # if sucsesffully opens file sets db_open to true
                
                db_open = True

            else: 

                file_path = input ('input path to file, include file name: ')



