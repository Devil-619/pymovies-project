# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:20:47 2020

@author: MEET
"""

from requests import get
from bs4 import BeautifulSoup
import requests
import pickle as pkl
rating=[]
info=[]
genre=[]
movies=[]
images=[]
summary=[]
information=[]
movie_name=input('Enter Movie name')
movies.append(movie_name)
url =input('Enter Movie URl')
response = get(url)
print(response.text[:500])

#Using BeautifulSoup to parse the HTML content

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

#Getting the rating
rating.append(html_soup.strong.span.text)



#Getting image url
image_url=html_soup.img.get('src')
images.append(image_url)
img_data = requests.get(image_url).content
with open(movie_name.replace(':','')+'.jpg', 'wb') as handler:
    handler.write(img_data)
    
    
    
#Getting summary
summary.append(html_soup.find('div',class_='summary_text').text)

#getting info  
info=html_soup.find_all('div',class_='credit_summary_item')
s=''
for i in info:
    print(i.h4.text)
    s +=i.h4.text +'\n'
    for j in i.find_all('a'):
        s +=j.text +'\n'
        print(j.text)
s=s.replace('See full cast & crew','')
information.append(s)

#getting genre
g=html_soup.find('div',class_='subtext').find_all('a')[:-1]
s=''
for i in g:
    s += i.text +'\n'
    print(i.text)
genre.append(s)    
