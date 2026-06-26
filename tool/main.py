from excell_read import read
from validation import validate
from sql_out import out
data = read()

clean_data = validate(data)

print (clean_data)