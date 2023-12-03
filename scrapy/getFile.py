import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

page = set()


def getLinks(url):
    global page
    html = urlopen('http://en.wikipedia.org{}'.format(url))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find({'id': 'mw-content-text'}).find_all('p'[0]))
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link['href'] not in page:
                newPage = link['href']
                print('-' * 20)
                page.add(link['href'])
                print(newPage)
                getLinks(newPage)


getLinks('')
