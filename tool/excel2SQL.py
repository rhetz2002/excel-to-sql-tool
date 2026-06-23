#imports required lib
import sqlite3 as sq
# defines output function

#grabs variables from main.py


def output_check ():
    
    db_open = False

    # user inputs path to file if no file exists one will be created

    file_path = input ('input path to file, include file name: ')

    while (db_open == False):
       
        try: 

            database = (file_path)

        finally: 

            if(input ('there is no file in this location do you want to create one?[Y/N]: ' == 'y' or 'Y')):

                print ('create file')







output_check()

