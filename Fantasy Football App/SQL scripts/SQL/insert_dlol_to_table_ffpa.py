import psycopg2
import pandas as pd
import pandas as pd
import numpy as np
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

cur = conn.cursor()

# download csv for fantasy points allowed from 4for4 website



# will parse this data, it will be changing thoughout the season
def parseDLOL():
    categories = ['ol','dl']
    website = 'https://www.footballoutsiders.com/stats/'
    
    
    oldl = []
    for each in categories:
        rank1,team_name,rank_num,dlranks = ([] for i in range(4))
        webpage = (str(website)+str(each))#changing categories to all vectors to see what happens
        page = urlopen(webpage) 
        soup = BS(page, 'html.parser')
        rank = soup.findAll('td')
        for i in rank:
            b = i.text.strip()
            rank1.append(b)
        new = (rank1)

        nn = 1
        while nn < 480:
            team_name.append(new[nn])
            nn+=15
        nnn = 12
        while nnn < 480:
            rank_num.append(new[nnn])
            nnn+= 15
        
        bb = 0
        while bb < 32:
            
            stat = [team_name[bb], rank_num[bb]]
            dlranks.append(stat)
            bb +=1
        
        dlranks.sort()
        oldl.append(dlranks)
    return oldl
# vector,vector,[team name,dfl,ofl]

dlol = parseDLOL()

i = 0

while i< 32:
    cur.execute("INSERT into fantasy_points_allowed(dfl)\
            VALUES ('{0}')".format((dlol[0][i][1])))
    conn.commit()
    i +=1

print("Data inserted successfully")

conn.close()
