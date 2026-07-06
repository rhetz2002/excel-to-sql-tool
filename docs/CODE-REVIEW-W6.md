## Code Review

- 1 excell_open.py line 41
  comparison to False should be 'if cond is False:' or 'if not cond:
  original: while opened == false
  corrected: while opened is false
  fixed in (removed whitespace in main.py and excell_open.py as well as changing "==" to "is" on line 41 of excell_open)

- 2 excell_open.py line 47 
  tool/excell_open.py:47:80: E501 line too long (113 > 79 characters)
  original: log = log + f'{time.strftime("%I:%M:%S %p")}: failed to open file in {file} reprompting user input\n'
  corrected: log = log + f'{time.strftime("%I:%M:%S %p")}: failed to ' \
                        f'open file in {file} reprompting user input\n'
  fixed in (shortened lines added FileError to except statements and removed unessasary whitespace)

- 3 SQL_output.py line 71
  tool/SQL_output.py:71:17: E128 continuation line under-indented for visual indent
  original: 
                db.execute("""
                        INSERT INTO employee_sales
                        (employee_ID, employee_name, employee_email, department, sales)
                        VALUES (?, ?, ?, ?, ?)""" ,
                (data_store[0], data_store[1], data_store[2], data_store[3], data_store[4]))
  corrected:
                db.execute("""
                           INSERT INTO employee_sales
                           (employee_ID, employee_name, employee_email, department, sales)
                           VALUES (?, ?, ?, ?, ?)""",
                           (data_store[0], data_store[1], data_store[2], data_store[3], data_store[4]))
  fixed in (removed exsess white spaces, shorttened lines, added FileError to except statement)

- 4 validation.py line 90
  tool/validation.py:90:80: E501 line too long (151 > 79 characters)
  original: log = log + f'{time.strftime("%I:%M:%S %p")}: row {index} fail on department check, pleas check that feild contains vaild department\n'
  corected: 
            log = log + f'{time.strftime("%I:%M:%S %p")}: row {index} ' \
                            f'fail on department check, pleas check that ' \
                            f'feild contains vaild department\n'
