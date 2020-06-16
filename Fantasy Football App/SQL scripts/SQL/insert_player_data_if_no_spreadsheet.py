import psycopg2
import pandas as pd
from create_cur import *
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

import requests



webpage = 'https://www.4for4.com/fantasy-football/tools/stat-app/touches/2019/1/3/ALL/ALL'

values = {'edit-name': 'mike_nb@sbcglobal.net',
          'edit-pass': 'FFFpw!@34'
          }
r = requests.post(webpage,data=values)
print(r.status_code)

page = urlopen(webpage)
soup = BS(page,'html.parser')
data = soup.findAll('tr', attrs={'class':'odd'})
data2 = soup.findAll('td')

print(soup)
