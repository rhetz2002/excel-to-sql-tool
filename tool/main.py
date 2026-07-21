# imports required packages and connects to
# external files adding core functions
from SQLcheck import SQL_check
from pathlib import Path
import argparse as arg
from excel_open import read
from SQLoutput import process
from validation import validate
import sqlite3 as sq
import time

# initiates var data_log to store operations log
# which will be exported to external log file

data_log = f'--------------------------------------------{time.strftime("%Y-%m-%d")}--------------------------------------------\n'

# initializes the CL input, initializing user_input  
# and the variables input and output, and finally
# args = user_input.parse_args with args being
# the variable to manipulate the user inputs

user_input = arg.ArgumentParser()
user_input.add_argument('input') 
user_input.add_argument('output')
args = user_input.parse_args()

# runs read from excel_open.py retrieving the 
# data from it in a tuple under data and log, data 
# is the excel data and log is the operations log
# passes the input through to read in excel_open

data, log = read(args.input)

# appends the log data from log to data_log for operations output when done 

data_log += log 

# passes args.output trough SQL_check in order to check that the output 
# location is valid, returns args.output as output variable in case it changes

log, output = SQL_check(args.output)

# like line 21 appends log data to data_log

data_log += log

# passes data variable through validate function from
# validation.py retrieving output data in tuple form 
# clean_data and log. clean data is verified data free
# of known errors. log is log file data

clean_data, log = validate(output, data)

# appends log data to data_log 

data_log += log

# runs clean_data through process function to insert into SQL database
# retrieves final log data in log variable 

log = process(output, clean_data)

# appends log data to data_log 

data_log += str(log)

# prints success in terminal indicating successful completion 

print('success')

# grabs absolute path from main.py 

absolute = Path('main.py').resolve()

# turns the path into a string to remove main.py from path stores in path_log

path_log = str(absolute).removesuffix('main.py') 

# tries to open using 'a' for append, will fail if doesn't exist 

try:
    
    # passes path through 'open' to open log file
    # appends 'log/operations.log' to the end of 
    # the path toproperly open file
    # stores file in operations variable



    operations = open(f'{path_log}log/operations.log', 'a')

    # passes 'data_log' through write to append to the end of log file
    
    operations.write(data_log)

    # closes log file

    operations.close

# executes if none exists 

except:
    

    # adds 'log' to the path and turns it back into a path that can be passed through 'mkdir'

    path_log = Path(path_log + ('log'))

    # runs mkdir on path_log to create the folder

    path_log.mkdir(parents=True, exist_ok=True)

    # opens the log file with 'w' to create the file, passes 'path_log through open alongside operations.log to complete the file path  

    operations = open(f'{path_log}/operations.log', 'w')

    # writes data_log into operations

    operations.write(data_log)

    # closes operations.log

    operations.close

