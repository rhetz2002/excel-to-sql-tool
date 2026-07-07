import pandas as pd
import time


# defines vaildate function
def validate(data):

    log = ''

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

                            int(row['ID'])
                        
                        except:

                            # if it is not an intiger sets check to four to set the error

                            check = 4

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

                        check = 3 

                else:
                
                    check = 2                            

            else:

                check = 1

            # checks if line is bad and which line is bad using 
            # the check variable                    

            if check == 0:

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

    print(f"{succsess} rows prossessed sucseffully")
    if fail >= 1:
        print(f'{fail} rows failed,')
        print(f'check operations log for more detail')
    print('--------------------------------------------')

    # stores passing data in clean
    
    clean = data.drop(bad_rows, axis=0)

    log = log + '--------------------------------------------\n'
    log = log + f'{time.strftime("%I:%M:%S %p")}\n'
    log = log + f'{succsess} rows prossessed sucseffully\n'
    log = log + f'{fail} rows failed\n'
    log = log + '--------------------------------------------\n'

    # returns clean
    return clean, log
