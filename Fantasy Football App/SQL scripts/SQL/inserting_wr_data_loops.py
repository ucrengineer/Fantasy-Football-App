import psycopg2
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

DB_NAME = "vassiqtl"
DB_USER = "vassiqtl"
DB_PASS = "QIM8NDA9Xp19kPDg4JpwQPrN87HoTIeL"
DB_HOST = "raja.db.elephantsql.com"
DB_PORT = "5432"

conn = psycopg2.connect(database = DB_NAME, user = DB_USER,
                        password=DB_PASS, host= DB_HOST,port=DB_PORT)


print("Database connected successfully")



def parseplayers():
    categories = ['QB','RB','WR','TE']
    website = 'https://www.footballdb.com/players/current.html?pos='
    total_data = []
    qbdata = []
    rbdata = []
    wrdata = []
    for each in categories:
        webpage = (str(website)+str(each))
        page = urlopen(webpage)
        soup = BS(page, 'html.parser')
        data = soup.findAll( attrs={'class':'td'})
        total_data.append(data)
    for each in total_data[0]:
        qb = each.text.strip()
        qbdata.append(qb)
    for each in total_data[1]:
        rb = each.text.strip()
        rbdata.append(rb)
    for each in total_data[2]:
        wr = each.text.strip()
        wrdata.append(wr)
    print("Data Gathered Successfully")
    return wrdata
    




wrdata = parseplayers()
wr_data = []
for each in wrdata:
    b = each.replace(" ","")
    bb = each.replace("'","")
    wr_data.append(bb)


cur = conn.cursor()
i = 0
while i < 1588:
    cur.execute("INSERT into nfl_player(id,name,team,pos) VALUES ('{0}','{1}','{2}','{3}')".format(i+337,wr_data[4*i],wr_data[4*i + 2],wr_data[4*i +1]))
    conn.commit()
    i+=1

print("Data inserted successfully")
conn.close()
