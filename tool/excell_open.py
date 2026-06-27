import datetime
import pandas as pd 
import time

def read():
    
    # variable to hold log text
    
    log = ''
    
    # variable to track if the user input a valid file path.
    # when a xlsx fiel is sucsessfully opened changes true

    opened = False
    
    #prompts user to input file path

    file = input('enter path to xlsx file: ')
    
    # atempts to open users input file path ment to fail if user inputs an invalid path

    try:
        
        data = pd.read_excel(file)
        
        # adds line to log that the file was sucsessfully opened including timestamp

        log = f'{time.strftime("%I:%M:%S %p")}: opened file in {file}\n'

        # sets oppened to true

        opened = True

    except:
        
        # check wether that opened is flase or true leaves loop if true

        while opened == False:
            
            # adds that user failed to open file to log 

            log = log + f'{time.strftime("%I:%M:%S %p")}: failed to open file in {file} reprompting user input\n'

            # promts user to re-enter file path with sugestion

            file = input('no file in directory please make sure u have the full file name including file extension: ')
            
            # another try except statement to check if input file is valid

            try:
                
                # trys to open file will fail and move to except statment if invalid

                data = pd.read_excel(file)
                
                # adds fact that file was sucsessfully opened to log

                log = log + f'{time.strftime("%I:%M:%S %p")}: opened file in {file}\n'
                
                # print file sucsesffuly opened to terminal

                print(f'{time.strftime("%I:%M:%S %p")}: opened file in {file}\n')

                # set opened to true

                opened = True

            except:
                
                # promts user to re-enter file path with sugestion

                log = log + f'{time.strftime("%I:%M:%S %p")}: failed to open file in {file} reprompting user input\n'
    
    return data, log