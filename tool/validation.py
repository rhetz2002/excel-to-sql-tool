import pandas as pd
import sqlite3 as sq
import time

def validate(filepath, data):    

    log = ''

    database = sq.connect(f"file:{filepath}?mode=rw", uri=True)

    db = database.cursor()
    
    db.execute("SELECT employee_ID FROM employee_sales")

    # stores ids in id_check

    id_check = [row[0] for row in db] 
    
    db.execute("SELECT employee_name FROM employee_sales")

    name_check = [row[0].strip() for row in db]

    success = 0

    fail = 0

    # iterates through the data taken from excel file
    # loops for the index and row
    omit_rows = []

    print("rows processed")
    print('--------------------------------------------')

    # used to check if a row is bad and which section of 
    # of the row is bad
    

    for index, row in data.iterrows():
        
        check = 0

        # thoroughly checks to see if its missing any
        # important data or formatted incorrectly
            
        # checks if ID column is not empty
        # if it is not valid sets check to one to set the error

        if pd.notna(row['ID']):
            
            # checks if name column is not empty, dose not contain a digit, 
            # is longer than 2 characters long, and has a space
            # if it is not valid sets check to two to set the error

            if pd.notna(row['name']) and not any(char.isdigit() for char in str(row['name'])) and len(str(row['name'])) >= 3 and ' ' in str(row['name']):

                # checks if email column is not empty, contains an @ symbol as well as .com, 
                # and is longer than nine characters
                # if it is not valid sets check to three to set the error

                if pd.notna(row['email']) and '@' in str(row['email']) and '.com' in str(row['email']) and len(str(row['email'])) >= 9:
                        
                    try: 

                        # checks that sales column is float

                        float(row['sales'])
                        
                    except: 

                        # if it is not a float sets check to six to set the error

                        check = 6    

                    # checks that department has a valid string

                    if pd.isna(row['department']) or str(row['department']).strip().lower() in ['sales', 'customer service', '']:


                        try:
                                
                                
                            # checks that ID column is an integer

                            if int(row['ID']) not in id_check:
                                
                                # adds one to success to keep track of valid rows
                            
                                success += 1                                
                                
                            elif str(row['name']).strip() in name_check:
                                    
                                db.execute("""
                                    UPDATE employee_sales
                                    SET employee_email = ?,
                                        department = ?,
                                        sales = ?
                                    WHERE employee_ID = ?""",
                                    (str(row['email']), str(row['department']).strip(), float(row['sales']), int(row['ID'])))

                                omit_rows.append(index)
                                
                                # adds one to success to keep track of valid rows
                            
                                success += 1     
                                    
                            else:

                                check = 4

                        except:

                            # if it is not an integer sets check to four to set the error

                            check = 4

                    else:
                            
                        # if it is not valid sets check to eight to set the error
                            
                        check = 8
                
                        

                else:

                    # if is missing, or is missing @, or missing 
                    # .com, or is less than 9 characters long
                    # sets check to 3 to set up for error message

                    check = 3 

            else:
                
                # if is missing or is less than 3 characters  
                # long or has digit or missing a space
                # sets check to 2 to set up for error message          

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
                
            # appends index of bad line to omit_rows list
                
            omit_rows.append(index)
                
            # resets check variable
                
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
                        f'field contains valid department\n'


    # prints pass fail message to terminal

    print(f"{success} rows processed successfully")
    if fail >= 1:
        print(f'{fail} rows failed,')
        print(f'check operations log for more detail')
    print('--------------------------------------------')

    # stores passing data in clean
    # while removing bad rows

    clean = data.drop(omit_rows, axis=0)

    # adds passing and failing lines to log

    log = log + '--------------------------------------------\n'
    log = log + f'{time.strftime("%I:%M:%S %p")}\n'
    log = log + f'{success} rows processed successfully\n'
    log = log + f'{fail} rows failed\n'
    log = log + '--------------------------------------------\n'
    
    # closes db

    database.close()
    
    # returns clean
    
    return clean, log
