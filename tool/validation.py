import pandas as pd
import time
import sqlite3 as sq


# defines vaildate function
def validate(file_path, data):

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
            
            database = sq.connect(f"file:{file_path}?mode=rw", uri=True)

            log = log + f'{time.strftime("%I:%M:%S %p")}: opened {file_path}\n'

            db = database.cursor()
            
            # sets db_open to true to end loop

            db_open = True

        except:

            # if opening fails asks user if they want to create file

            if input('there is no file in this location '
                     'do you want to create one?[Y/N]: ').lower() == 'y':

                # creates file

                f'{time.strftime("%I:%M:%S %p")}: created ' \
                    f'new database file in {file_path}\n'

                # creates db from input file path
                
                database = sq.connect(file_path)

                # initiates coursor as db

                db = database.cursor()

                # executes SQL here to create the data tables

                # im sure that theres a way to create
                # the table depending on the contents
                # of the xlsx file but for the puroposes
                # of the asignment ill just hard code it
                
                log = log + f'{time.strftime("%I:%M:%S %p")}: sucseffully ' \
                            f'created database in {file_path}\n'

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

            # else to reprompt user to input path

            else:

                # if user selects no in last prompt,
                # prompts user to input path to sql file again

                file_path = input('input path to database file, include file name: ')

    # executes select to grab emploee ids

    db.execute("SELECT employee_ID FROM employee_sales")

    # stores ids in id_check

    id_check = [row[0] for row in db] 

    #--------------------------
    # temp to check ids stored
    #--------------------------

    print(id_check)

    succsess = 0

    fail = 0

    # iterates through the data taken from excell file
    # loops for the index and row
    bad_rows = []

    print("rows processed")
    print('--------------------------------------------')

    # used to check if a row is bad and which section of 
    # of the row is bad
    check = 0

    for index, row in data.iterrows():

            # thuroughly checks to see if its missing any
            # important data or formated incorectly
            
            # checks if ID collomn is not empty
            # if it is not valid sets check to one to set the error

            if pd.notna(row['ID']):
                
                # checks if name collomn is not empty, dose not contain a digit, 
                # is longer than 2 charicters long, and has a space
                # if it is not valid sets check to two to set the error

                if pd.notna(row['name']) and not any(char.isdigit() for char in str(row['name'])) and len(str(row['name'])) >= 3 and ' ' in str(row['name']):

                    # checks if email collomn is not empty, contains an @ symbol as well as .com, 
                    # and is longer than nine charicters
                    # if it is not valid sets check to three to set the error

                    if pd.notna(row['email']) and '@' in str(row['email']) and '.com' in str(row['email']) and len(str(row['email'])) >= 9:
                        
                        try: 

                            # checks that ID colomn is an intiger

                            if int(row['ID']) not in id_check:

                                
                                try:

                                    # checks that sales colounm is float

                                    float(row['sales'])
                        
                                except: 

                                    # if it is not a float sets check to six to set the error

                                    check = 6    

                                # checks that department has a valid string

                                if str(row['department']) in ['sales', 'customer service']:
                            
                                    # adds one to succsess to keep track of valid rows
                            
                                    succsess = succsess + 1

                                else:
                            
                                    # if it is not valid sets check to eight to set the error
                            
                                    check = 8

                            else:

                                # if it is alredy in the db sets check to four to set the error

                                check = 4

                        except:

                            # if it is not an intiger sets check to four to set the error

                            check = 4

                    else:

                        # if is missing, or is missing @, or missing 
                        # .com, or is les than 9 charicters long
                        # sets check to 3 to set up for error mesage

                        check = 3 

                else:
                
                    # if is missing or is less than 3 charicters  
                    # long or has digit or missing a space
                    # sets check to 2 to set up for error mesage       

                    check = 2                            

            else:

                # if missing sets check to 1 to set up for error message

                check = 1

            # checks if line is bad and which line is bad using 
            # the check variable                    

            if check == 0:
                
                # if no errors
                # adds one to sucsess to keep track of number good lines
                
                print(f"row {index} sucsess")

            else: 

                #prints which row pass and fail
                # adds 1 to fail to keep track of number of bad lines
                
                fail = fail + 1
                print(f"row {index} fail")
                
                # appends index of bad line to bad_rows list
                
                bad_rows.append(index)
                
                # resets check variable
                
                check = 0

            # uses check to see what part of line failed to insert into
            
            if check == 1 or check == 4:

                log = log + f'{time.strftime("%I:%M:%S %p")}: row ' \
                            f'{index} fail on ID check, pleas check ' \
                            f'that ID is present, is int, or not duplicated\n'
                
            elif check == 2:

                log = log + f'{time.strftime("%I:%M:%S %p")}: row ' \
                            f'{index} fail on name check, pleas ' \
                            f'check that name is present\n'

            elif check == 3:

                log = log + f'{time.strftime("%I:%M:%S %p")}: row {index}' \
                            f' fail on email check, pleas check that email ' \
                            f'is present and is in proper format\n'

            elif check == 6:

                log = log + f'{time.strftime("%I:%M:%S %p")}: row {index}' \
                            f' fail on sales check,' \
                            f' pleas check that sales is int\n'

            elif check == 8:

                log = log + f'{time.strftime("%I:%M:%S %p")}: row {index} ' \
                            f'fail on department check, pleas check that ' \
                            f'feild contains vaild department\n'

    # prints pass fail mesage to terminal

    print(f"{succsess} rows prossessed sucseffully")
    if fail >= 1:
        print(f'{fail} rows failed,')
        print(f'check operations log for more detail')
    print('--------------------------------------------')

    # stores passing data in clean
    # while removing bad rows
    
    clean = data.drop(bad_rows, axis=0)

    # adds passing and failing lines to log

    log = log + '--------------------------------------------\n'
    log = log + f'{time.strftime("%I:%M:%S %p")}\n'
    log = log + f'{succsess} rows prossessed sucseffully\n'
    log = log + f'{fail} rows failed\n'
    log = log + '--------------------------------------------\n'

    # returns clean
    return clean, log
