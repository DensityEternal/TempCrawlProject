import datetime
import random
import requests
import time
from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup

web_url = r'http://www.imooc.com'
html = urlopen(web_url)
bs = BeautifulSoup(html, 'html.parser')
random.seed(datetime.datetime.now().timestamp())
web_url=web_url+'/course/list?ct=1&page='+'1'
print(web_url)
bs = BeautifulSoup(urlopen(web_url), 'html.parser')
cover = bs.findAll('img')

for c in cover:
    time.sleep(1)
    response=requests.get(web_url+c['src'])
    filename=c['src'].split('/')[-1]
    urlretrieve(web_url+c['src'],'log.jpg')
    with open(filename,'wb')as f:
        f.write(response.content)
"""    Address=c.attrs['style']
    start = Address.find('(') + 1
    end = Address.find(')')
    url = Address[start:end]

    filename = url.split('/')[-1].split('\'')[0]
    print(filename)
    finalUrl = web_url+ url.split('\'')[1]
    print(finalUrl)
    response=requests.get(finalUrl)
    with open('scrapyImage/'+filename, 'wb')as f:
        f.write(response.content)

for i in range(1,24):
    web_url=web_url+'/course/list?ct=1&page=' + str(i)
    bs=BeautifulSoup(urlopen(web_url),'html.parser')
    cover=bs.findAll('div', {"class":"img"})"""

"""def getLinks(other_url):
    html = urlopen(web_url + f'{other_url}')
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'class': 'course-list'}).find_all(lambda tag: len(tag.attrs) == 6)


"""

"""
externalUrl = []
try:
    for i in range(1, 23):
        links = getLinks('/course/list?ct=1&page=' + str(i))

        for i in range(40):
            newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
            externalUrl.append('http:'+newArticle)
except AttributeError:
    pass
print(externalUrl[1])"""