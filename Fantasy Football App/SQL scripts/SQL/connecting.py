import psycopg2

DB_NAME = "vassiqtl"
# removed my database user information
DB_USER = "user name"
DB_PASS = "password"
DB_HOST = "raja.db.elephantsql.com"
DB_PORT = "5432"


try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                            password=DB_PASS, host= DB_HOST,port=DB_PORT)


    print("Database connectd successfully!!")


except:
    print("Database not connected")
