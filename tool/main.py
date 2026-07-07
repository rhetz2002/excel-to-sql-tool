# imports required packages and conects to
# external files adding core functions

from excell_open import read
from SQL_output import prossess
from validation import validate
import sqlite3 as sq
import time

# initates var data_log to store operations log
# which will be exported to external log file

data_log = f'--------------------------------------------{time.strftime("%Y-%m-%d")}--------------------------------------------\n'

# runs read from excell_open.py retreving the
# data from it in a tupple under data and log data
# is the excell data and log is the operations log

data, log = read()

# apeneds the log data from log to data_log for "running total?"

data_log = data_log + log

# pases data variable through vailidate function from
# validation.py retreving output data in tupple form
# clean_data and log. clean data is verified data free
# of known errors. log is log file data

clean_data, log = validate(data)

print (clean_data)
# like line 21 appeneds log data to data_log

data_log = data_log + log

# runs clean_data through process function to insert into sql database
# retreives final log data in log variable

log = prossess(clean_data)

# appeneds log data to data_log

data_log = data_log + str(log)

# prints succsess in terminal indicating sucsessfull completion

print('sucsess')

# trys to open using x for exclusive creation, will fail if alredy exsists

try:
    operations = open('log/operations.log', 'x')

    operations.write(data_log)

    operations.close

# if alredy exsists openes with a for append

except:
    operations = open('log/operations.log', 'a')

    operations.write(data_log)

    operations.close()

# after opening writes data_log into operations.log

