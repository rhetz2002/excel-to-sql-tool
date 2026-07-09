import sqlite3 as sq
import time

# defines output function


def prossess(file_path, data):

    # initiates log variable

    log = ''

    # stores data from data variable

    data_store = []

    database = sq.connect(f"file:{file_path}?mode=rw", uri=True)

    db = database.cursor()

    # iterates over the data in data

    for index, row in data.iterrows():

        # reads row by row adds to data_store

        data_store.append(data.at[index, 'ID'])

        data_store.append(data.at[index, 'name'])

        data_store.append(data.at[index, 'email'])

        data_store.append(data.at[index, 'department'])

        data_store.append(float(data.at[index, 'sales']))

        # executes SQL adding the data_store data into the SQL

        db.execute("""
                    INSERT INTO employee_sales
                    (employee_ID, employee_name, employee_email, department, sales)
                    VALUES (?, ?, ?, ?, ?)""",
                    (data_store[0], data_store[1], data_store[2], data_store[3], data_store[4]))

        # resets data_store

        data_store = []

    log = log + f'{time.strftime("%I:%M:%S %p")}: sucseffully ' \
                        f'inserted data from xlsx to {file_path}\n'

    # commits and closes database

    database.commit()
    db.close()

    return log
