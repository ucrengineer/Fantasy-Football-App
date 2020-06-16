import sqlite3

## can pass in filename in ()
## now creates the .db file
conn = sqlite3.connect('employee.db')

# now can start running sql commands
c = conn.cursor()

#create a employee table, first name column and data type

# """ are doc strings that can be continuous"""
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

# need to commit the current transaction
conn.commit()


# now close connection to database

conn.close()
