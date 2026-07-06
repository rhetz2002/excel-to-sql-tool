import pandas as pd
import time


# defines vaildate function
def validate(data):

    log = ''

    succsess = 0

    fail = 0

    # iterates through the data taken from excell file
    # loops for the index and row
    bad_rows = []

    print("rows processed")
    print('--------------------------------------------')

    check = 0

    for index, row in data.iterrows():

        # sees if is int or int adjacent

        try:

            # thuroughly checks to see if its missing any
            # important data or formated incorectly

            if pd.notna(row['ID']):

                check = 1

                if pd.notna(row['name']):

                    check = 2

                    if pd.notna(row['email']):

                        check = 3

                        if int(row['ID']):

                            check = 4

                            if str(row['name']):

                                check = 5

                                if float(row['sales']):

                                    check = 6

                                    if '@' in str(row['email']):

                                        check = 7

                                        if str(row['department']) in ['sales', 'customer service']:
                                            print(f"row {index} sucsess")

                                            check = 0

                                            succsess = succsess + 1

        # if fails check, stores index in list to be removed at end
        # also prints which row pass and fail

        except ValueError:

            if check == 0 or check == 3:

                log = log + f'{time.strftime("%I:%M:%S %p")}: row ' \
                            f'{index} fail on ID check, pleas check ' \
                            f'that ID is present, is int, or not duplicated\n'

            elif check == 1 or check == 4:

                log = log + f'{time.strftime("%I:%M:%S %p")}: row ' \
                            f'{index} fail on name check, pleas ' \
                            f'check that name is present\n'

            elif check == 2 or ckeck == 6:

                log = log + f'{time.strftime("%I:%M:%S %p")}: row {index}' \
                            f' fail on email check, pleas check that email ' \
                            f'is present and is in proper format\n'

            elif check == 5:

                log = log + f'{time.strftime("%I:%M:%S %p")}: row {index}' \
                            f' fail on sales check,' \
                            f' pleas check that sales is int\n'

            else:

                log = log + f'{time.strftime("%I:%M:%S %p")}: row {index} ' \
                            f'fail on department check, pleas check that ' \
                            f'feild contains vaild department\n'

            bad_rows.append(index)

            fail = fail + 1

    print(f"{succsess} rows prossessed sucseffully")
    if fail >= 1:
        print(f'{fail} rows failed,')
        print(f'check operations log for more detail')
    print('--------------------------------------------')

    # stores passing data in clean
    clean = data.drop(bad_rows, axis=0)

    log = log + '--------------------------------------------\n'
    log = log + f'{time.strftime("%I:%M:%S %p")}\n'
    log = log + f'{succsess} rows prossessed sucseffully\n'
    log = log + f'{fail} rows failed\n'
    log = log + '--------------------------------------------\n'

    # returns clean
    return clean, log
