import psycopg2

def CreateNflPlayerTable():
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
#Creating nfl_players table

    cur.execute("""

CREATE TABLE nfl_player
(

id INT NOT NULL,
name VARCHAR(40),
pos VARCHAR(8),
team VARCHAR(40),
tchs_atts SMALLINT,
PRIMARY KEY (id)
)

""")

    conn.commit()
    print("Table Created Successfully")
