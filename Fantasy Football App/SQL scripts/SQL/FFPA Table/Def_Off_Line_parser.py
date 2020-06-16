import psycopg2
import pandas as pd
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen







def parseDLOL():
    categories = ['ol','dl']
    website = 'https://www.footballoutsiders.com/stats/'
    team,rank,dl = ([] for i in range(3))
    
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
        print(new[28])

        i=12
        counter = 0
        while i < len(new) and counter <32:
            team_name.append(new[i])
            rank_num.append(new[i+1])
            print(team_name)
            print(rank_num)
            
            i+=16
            counter+=1

        
parseDLOL()
