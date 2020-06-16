import psycopg2
import pandas as pd

DB_NAME = "vassiqtl"
DB_USER = "vassiqtl"
DB_PASS = "QIM8NDA9Xp19kPDg4JpwQPrN87HoTIeL"
DB_HOST = "raja.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                        password=DB_PASS, host= DB_HOST,port=DB_PORT)

cur = conn.cursor()
print("Database connected successfully")



# download csv file from 4for4 website on qb,rb,wr,te touches.
# https://www.4for4.com/fantasy-football/tools/stat-app/touches/2019/1/1/ALL/ALL

def readcsvfile(file):
    df = pd.read_csv(file)
    name = df['Player']
    pos = df['Pos']
    team = df['Team']
    TCHs = df['TCHs']

    return (name,pos,team,TCHs)
    

nam,pos,team,TCHs = readcsvfile(r'C:/Users/moffe/Downloads/4for4-fantasy-football-tools-stat-app-touches-2019-1-4-ALL-ALL-table.csv')
name = []
for each in nam:
    b = each.replace("'","")
    name.append(b)

print("Data read successfully")

i = 0
while i < len(name):
        try:
            cur.execute("INSERT into nfl_player(id,name,\
                pos,team,tchs_atts)\
                VALUES ('{0}','{1}','{2}','{3}','{4}'\
                )".format(i+48,name[i],pos[i],team[i],TCHs[i]))
            conn.commit()
            i+=1
        except Exception as e:
            
            print('%s, connection terminated' %e)
            conn.close()

print("Data inserted successfully")
conn.close()
