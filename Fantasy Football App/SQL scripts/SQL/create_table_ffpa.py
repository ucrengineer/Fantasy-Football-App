import psycopg2

def createffpatable():
    DB_NAME = "vassiqtl"
    DB_USER = "vassiqtl"

    # removed my database user information
    DB_USER = "user name"
    DB_PASS = "password"

    DB_PORT = "5432"

    conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                        password=DB_PASS, host= DB_HOST,port=DB_PORT)


    print("Database connected successfully")

    cur = conn.cursor()


    cur.execute("""

    CREATE TABLE fantasy_points_allowed
    (

    id INT NOT NULL,
    team VARCHAR(5),
    qb_rank SMALLINT,
    rb_rank SMALLINT,
    rbppr_rank SMALLINT,
    wr_rank SMALLINT,
    wrppr_rank SMALLINT,
    te_rank SMALLINT,
    teppr_rank SMALLINT,
    def_ranks SMALLINT,
    dfl SMALLINT,
    ofl SMALLINT,
    short SMALLINT,
    deep SMALLINT,
    off_pace SMALLINT,
    PRIMARY KEY (id)
    )

    """)

    conn.commit()
    conn.close()
    print("Table Created Successfully")
