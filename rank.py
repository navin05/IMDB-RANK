# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:07:35 2020

@author: User
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

req = urlopen('https://www.imdb.com/chart/top/').read()


soup = BeautifulSoup(req, 'html.parser')

Rank = []
Title = []
Rating = []

Ran = soup.findAll('td',attrs={"class":"titleColumn"})
a = soup.find_all('td',attrs={"class":"ratingColumn imdbRating"})
for i in range(0,len(Ran)):
    
    r = Ran[i].text.strip()
    # print(r.split('.')[1])
    Rank.append(r.split('.')[0])
    Title.append(Ran[i].find('a').text.strip())
for j in range(0,len(a)):
    print(a[j].text.strip())
    Rating.append(a[j].text.strip())
    
scrape = pd.DataFrame({'Rank':Rank,'Title':Title,'Rating':Rating})
scrape.to_csv('imdb.csv',index=False)