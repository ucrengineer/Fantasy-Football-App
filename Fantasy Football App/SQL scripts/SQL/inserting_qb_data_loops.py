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
    rb_data = []
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
        rb_data.append(rb)
    print("Data Gathered Successfully")
    return qbdata
    




qbdata = parseplayers()
qb_data = []
for each in qbdata:
    b = each.replace(" ","")
    qb_data.append(b)


cur = conn.cursor()
i = 0
while i < 480:
    cur.execute("INSERT into nfl_player(id,name,team,pos) VALUES ('{0}','{1}','{2}','{3}')".format(i,qb_data[4*i],qb_data[4*i + 2],qb_data[4*i +1]))
    conn.commit()
    i+=1

print("Data inserted successfully")
conn.close()
