import psycopg2

def droptable(tablename):
    # removed my database login information
    DB_NAME = "vassiqtl"
    DB_USER = "username"
    DB_PASS = "password"
    DB_HOST = "raja.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                        password=DB_PASS, host= DB_HOST,port=DB_PORT)


    print("Database connected successfully")

    cur = conn.cursor()

    cur.execute("DROP TABLE %s" %tablename)
    conn.commit()
    print("%s Database is reset" %tablename)
