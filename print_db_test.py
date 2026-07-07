import sqlite3

# 1. Connect to the database file (replace with your file name)
conn = sqlite3.connect('tool/output/db.db')
cursor = conn.cursor()

# 2. Execute a SELECT statement on your table
cursor.execute("SELECT * FROM employee_sales")

# 3. Fetch all rows and print them one by one
rows = cursor.fetchall()
for row in rows:
    print(row)

# 4. Close the connection
conn.close()
