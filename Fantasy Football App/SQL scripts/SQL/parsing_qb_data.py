from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import psycopg2
from nfl_players_create_table import CreateNflPlayerTable as plytable
from DropTable import *
from create_cur import *


cur, conn = connect_curr()

droptable('nfl_player')
plytable()

#website = 'http://www.nfl.com/stats/categorystats?tabSeq=1&season=2019&seasonType=REG&experience=&Submit=Go&archive=false&conference=null&d-447263-p=1&statisticPositionCategory=QUARTERBACK&qualified=true'
#websit2 = 'http://www.nfl.com/stats/categorystats?tabSeq=1&season=2019&seasonType=REG&Submit=Go&experience=&archive=false&conference=null&d-447263-p=2&statisticPositionCategory=QUARTERBACK&qualified=true'
part1 = 'http://www.nfl.com/stats/categorystats?tabSeq=1&season=2019&seasonType=REG&experience=&Submit=Go&archive=false&conference=null&d-447263-p='
part2 = '&statisticPositionCategory=QUARTERBACK&qualified=true'
# only 1 page right now, pages = ['1','2']
pages = ['1']
name,team,pos,att = ([] for i in range(4))
for each in pages:
    
    qb_data = []
    test = []
    webpage = part1 + each + part2
    page = urlopen(webpage)
    soup = BS(page, 'html.parser')
    data = soup.findAll('tr', attrs={'class':'odd'})
    data2 = soup.findAll('td')
    for each in data2:
        b = each.text.strip()
        bb = b.replace("\n","")
        test.append(bb)
    for each in test:
        qb_data.append(each)


    i= 0
    while i < (len(qb_data)/10):
        name.append(qb_data[10*i + 1])
        i += 2

    ii = 0
    while ii < (len(qb_data)/10):
        team.append(qb_data[10*ii + 2])
        ii +=2

    b = 0
    while b < (len(qb_data)/10):
        pos.append(qb_data[10*b + 3])
        b += 2


    bb = 0
    while bb < (len(qb_data)/10):
        att.append(qb_data[10*bb + 5])
        bb+= 2


print("Data read successfully")
cur = conn.cursor()

i = 0
try:
    while i < len(name):
        cur.execute("INSERT into nfl_player(id,name,\
                pos,team,tchs_atts)\
                VALUES ('{0}','{1}','{2}','{3}','{4}'\
                )".format(i,name[i],pos[i],team[i],att[i]))
        conn.commit()
        i+=1
        print('Players Uploaded: %s' %name[i])
except:
    print("Data inserted successfully")
    conn.close()

