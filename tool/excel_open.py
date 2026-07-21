import datetime
import pandas as pd
import time



def read(file):

    # variable to hold log text

    log = ''

    # variable to track if the user inputs a valid file path. 
    # When a xlsx file is successfully opened changes true 

    opened = False

    # attempts to open users input file path 
    # meant to fail if user inputs an invalid path 
    
    # loop continues until try succeeds and opened is true 

    while not opened:
        
        # tries to open file, if fails to open it triggers a re-prompt in except 

        try:
            
            # attempt to open file stores file data in data variable

            data = pd.read_excel(file)

            # adds line to log that the file was
            # successfully opened including timestamp 

            log = f'{time.strftime("%I:%M:%S %p")}: opened file in {file}\n'

            # sets opened to true 

            opened = True

        except:

            # adds that user failed to open file to log

            log += f'{time.strftime("%I:%M:%S %p")}: failed to ' \
                   f'open file in {file} re-prompting user input\n' 

            # prompts user to re-enter file path with suggestion 

            file = input('no input file in directory please make sure u have ' 
                         'the full file name including file extension, usually .xlsx: ')  

    return data, log
