#imports required lib
import sqlite3 as sq


#grabs variables from main.py

# defines output function

def output_check ():
    
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

            # atempts to open file, purpoussfully made to fail if its not there as a qol feature 
            # as a mesure to make sure the user knows that its not typed in corectly if fails and alredy exsists

            database = sq.connect(file_path,mode=rw)

            # if sucsesffully opens file sets db_open to true

            db_open = True

        except: 
            
            # if opening fails asks user if they want to create file

            if input ('there is no file in this location do you want to create one?[Y/N]: ').lower() == 'y' :

                print('file created in directory')

                #creates file
                database = sq.connect(file_path)

                db = database.cursor()

                db.execute(""" CREATE TABLE employee_sales (                                           
                                         
                                employee_ID int PRIMARY KEY NOT NULL,
                                employee_name text NOT NULL,
                                employee_email text NOT NULL,
                                department text,
                                sales real)
                
                            """)                                                          
                
                # will import the sql data here 

                database.commit()
                db_open = True



            else: 

                file_path = input ('input path to file, include file name: ')








output_check()

