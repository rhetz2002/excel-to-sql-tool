import datetime
import pandas as pd
import time


def read(file):

    # variable to hold log text

    log = ''

    # variable to track if the user input a valid file path.
    # when a xlsx fiel is sucsessfully opened changes true

    opened = False

    # atempts to open users input file path
    # ment to fail if user inputs an invalid path
    
    # loop continues untill try sucseeds and opened == true

    while not opened:
        
        # trys to open file if fails to open triggers reprompt in except

        try:
            
            # attempt to open file stores file data in data variable

            data = pd.read_excel(file)

            # adds line to log that the file was
            # sucsessfully opened including timestamp

            log = f'{time.strftime("%I:%M:%S %p")}: opened file in {file}\n'

            # sets oppened to true

            opened = True

        except:

            # adds that user failed to open file to log

            log = log + f'{time.strftime("%I:%M:%S %p")}: failed to ' \
                        f'open file in {file} reprompting user input\n'

            # promts user to re-enter file path with sugestion

            file = input('no file in directory please make sure u have '
                         'the full file name including file extension: ')

    return data, log
