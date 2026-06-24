import pandas as pd 

def read():
    
    # initalisez gloabal variable that will be sent back to main file

    # opens excell, will pull path from main in future

    data = pd.read_excel('input/input.xlsx')

    # stores in variable
    print(data)
    # closes file

read()