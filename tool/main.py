# imports required packages and conects to
# external files adding core functions
from pathlib import Path
import argparse as arg
from excell_open import read
from SQL_output import prossess
from validation import validate
import sqlite3 as sq
import time

# initates var data_log to store operations log
# which will be exported to external log file

data_log = f'--------------------------------------------{time.strftime("%Y-%m-%d")}--------------------------------------------\n'

# inistalises the CL input, initallising user_input
# and the variables input and output, and finally
# args = user_input.parse_args with args being
# the variable to manipulate the user inputs

user_input = arg.ArgumentParser()
user_input.add_argument('input') 
user_input.add_argument('output')
args = user_input.parse_args()

# runs read from excell_open.py retreving the
# data from it in a tupple under data and log data
# is the excell data and log is the operations log

# passes the input through too read in excell_open

data, log = read(args.input)

# apeneds the log data from log to data_log for "running total?"

data_log = data_log + log

# pases data variable through vailidate function from
# validation.py retreving output data in tupple form
# clean_data and log. clean data is verified data free
# of known errors. log is log file data

clean_data, log, output = validate(args.output, data)

print (clean_data)
# like line 21 appeneds log data to data_log

data_log = data_log + log

# runs clean_data through process function to insert into sql database
# retreives final log data in log variable

log = prossess(output, clean_data)

# appeneds log data to data_log

data_log = data_log + str(log)

# prints succsess in terminal indicating sucsessfull completion

print('sucsess')

# trys to open using a for for append, will fail if alredy exsists

try:
    
    operations = open('log/operations.log', 'a')

    operations.write(data_log)

    operations.close

# if none exsists tool will grab absolute path from main.py
except:
    
    absolute = Path('main.py').resolve()

    # turns the path into a string to remove main.py from path

    path_log = str(absolute).removesuffix('main.py') 

    # adds 'log' to the path and turns it back into a path that can be passed through 'mkdir'

    path_log = Path(path_log + ('log'))

    # runs mkdir on path_log to create the folder

    path_log.mkdir(parents=True, exist_ok=True)

    # opens the log file with w to create the file, passes 'path_log through open alongside operations.log to compleet the file path 

    operations = open(f'{path_log}/operations.log', 'w')

    operations.write(data_log)

    operations.close

