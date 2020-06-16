import psycopg2
import pandas as pd
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
from create_table_ffpa import *
from DropTable import *
from create_cur import *



# download csv for fantasy points allowed from 4for4 website
# https://www.4for4.com/fantasy-football/reports/sos/adjusted
def readcsvfile(file):
    df = pd.read_csv(file)
    teams = df['Team']
    qb_ranks = df['#']
    rb_ranks = df['#.1']
    rbppr_ranks = df['#.2']
    wr_ranks = df['#.3']
    wrppr_ranks = df['#.4']
    te_ranks = df['#.5']
    teppr_ranks = df['#.6']
    def_ranks = df['#.10']
    return (teams,qb_ranks,rb_ranks,rbppr_ranks,wr_ranks,wrppr_ranks,te_ranks,teppr_ranks,def_ranks)
    

    print("Data read successfully")
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

        nn = 12
        counter = 0
        while nn < len(new) and counter < 32:
            team_name.append(new[nn])
            nn+=16
        nnn = 13
        while nnn < len(new) and counter < 32:
            rank_num.append(new[nnn])
            nnn+= 16
        
        bb = 0
        while bb < 32:
            
            stat = [team_name[bb], rank_num[bb]]
            dlranks.append(stat)
            bb +=1
        
        dlranks.sort()
        oldl.append(dlranks)
        
    return oldl
# vector,vector,[team name,dfl,ofl]
    print("Offensive/Defensive lines parsed successfully")

# parse this data, it will be changing throughout the season
def parseDS():

    dnumbers,numbers,short,deep,DS,letters,teams = ([] for i in range(7))
    category = 'teamdef'
    website = 'https://www.footballoutsiders.com/stats/'
    webpage = (str(website)+str(category))
    page = urlopen(webpage)
    soup = BS(page,'html.parser')

    raw = soup.findAll('td' , attrs={'align':'center'})
    raw2 = soup.findAll('td')
    raw3 = soup.findAll('td', attrs={'align':'Right'})
    #gather order of teams
    for each in raw2:
        b = each.text.strip()
        letters.append(b)
    
    nn = 1271
    while nn < 1848:
        teams.append(letters[nn])
        nn += 18
    #gather the 'short' rank
    for each in raw:
        b = each.text.strip()
        numbers.append(b)
    n = 1
    while n < 166:
        bb =(numbers[n])
        short.append(bb)
        n+=5
    #gather the 'deep' rank
    for each in raw3:
        bbb = each.text.strip()
        dnumbers.append(bbb)
    n = 1147
    while n < 1490:
        deep.append(dnumbers[n])
        n+=11
    #allign data
    p = 0

    while p < 32:
        ds = [teams[p], short[p], deep[p]]
        DS.append(ds)
        p+=1
  
    DS.sort()
    return DS
# [Team name, short, and then deep]
    print("Short/Deep data parsed successfully")
try:
    droptable('fantasy_points_allowed')
except:
    print('FFPA Table being created')

createffpatable()
dlol = parseDLOL()
#DS = parseDS(), There is a error with this function, will fix later
#https://www.footballoutsiders.com/premium/defense-by-pass-direction?year=2019&offense_defense=offense
#Had to put data in manually, will find a better way later. For now, this will have to do. Alphebetically in order
Short = [29,27,14,2,16,19,31,18,22,21,11,5,25,28,8,6,26,15,32,10,3,20,13,4,12,17,23,24,1,7,9,30]
Deep = [22,17,29,3,1,9,30,4,10,20,8,6,13,25,21,14,19,7,32,16,2,31,26,23,28,12,27,11,15,18,24,5]
#Another manual entry lol..alphebetically ordered
Off_Pace = [1,8,19,16,2,24,7,25,20,5,12,17,23,11,29,6,30,3,4,26,21,31,9,28,32,14,13,27,18,15,22,10]
###################   
teams,qb_ranks,rb_ranks,rbppr_ranks,wr_ranks,wrppr_ranks,te_ranks,teppr_ranks,def_ranks = readcsvfile(r'C:/Users/moffe/Downloads/4for4-fantasy-football-reports-sos-adjusted-table (4).csv')
print("Functions loaded properly")
cur,conn = connect_curr()
i = 0
# replacing DS[i][1],DS[i][2] with DS[i] for now!!!!
while i < 32:
    cur.execute("INSERT into fantasy_points_allowed(id,team,\
qb_rank,rb_rank,rbppr_rank,wr_rank,wrppr_rank,te_rank,teppr_rank,\
def_ranks,dfl,ofl,short,deep,off_pace) VALUES ('{0}','{1}','{2}','{3}',\
'{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}')\
".format(i,teams[i],qb_ranks[i],rb_ranks[i],rbppr_ranks[i],wr_ranks[i],\
wrppr_ranks[i],te_ranks[i],teppr_ranks[i],def_ranks[i],dlol[1][i][1],dlol[0][i][1],Short[i],Deep[i],Off_Pace[i]))
    conn.commit()
    i+=1

print("Data inserted successfully")
conn.close()
