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
