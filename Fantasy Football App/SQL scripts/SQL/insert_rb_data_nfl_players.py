import psycopg2
import pandas as pd

DB_NAME = "vassiqtl"
DB_USER = "vassiqtl"
DB_PASS = "QIM8NDA9Xp19kPDg4JpwQPrN87HoTIeL"
DB_HOST = "raja.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                        password=DB_PASS, host= DB_HOST,port=DB_PORT)


print("Database connected successfully")

cur = conn.cursor()



def readcsvfile(file):
    df = pd.read_csv(file)
    name = df['Player']
    pos = df['Pos']
    team = df['Team']
    TCHs = df['TCHs']

    return (name,pos,team,TCHs)
    

nam,pos,team,TCHs = readcsvfile(r'C:\Users\moffe\Desktop\Python Programs\python v3 programs\Fantasy Football Program\rb_info.csv')
name = []
for each in nam:
    b = each.replace("'","")
    name.append(b)

print("Data read successfully")
i = 0
while i < len(name):
    cur.execute("INSERT into nfl_player(id,name,\
                pos,team,tchs)\
                VALUES ('{0}','{1}','{2}','{3}','{4}'\
                )".format(i,name[i],pos[i],team[i],TCHs[i]))
    conn.commit()
    i+=1

print("Data inserted successfully")
conn.close()
