from bs4 import BeautifulSoup as BS
from urllib.request import Request,urlopen



def parseDS():

    dnumbers,numbers,short,deep,DS,letters,teams = ([] for i in range(7))
    category = 'offense'
    website = 'https://www.footballoutsiders.com/premium/defense-by-pass-direction?year=2019&offense_defense='
    webpage = Request(str(website)+str(category),headers = {'User-Agent':'Mozilla/5.0'})
    
    page = urlopen(webpage).read()
    soup = BS(page,'html.parser')
    print(soup)
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

ds = parseDS()
print(ds)
