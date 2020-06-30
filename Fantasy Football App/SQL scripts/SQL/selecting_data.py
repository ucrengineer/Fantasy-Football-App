import psycopg2

DB_NAME = "vassiqtl"
# removed my database user information
DB_USER = "user name"
DB_PASS = "password"
DB_HOST = "raja.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                        password=DB_PASS, host= DB_HOST,port=DB_PORT)


print("Database connected successfully")

cur = conn.cursor()


cur.execute("SELECT ID,NAME,EMAIL FROM Employee")

row = cur.fetchall()

for data in row:
    print("ID : " + str(data[0]))
    print("NAME : " + data[1])
    print("Email "  + data[2])



print("Data Selected Successfully")
conn.close()
