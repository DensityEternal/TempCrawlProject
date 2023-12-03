import json
import threading

import requests
from bs4 import BeautifulSoup as bs


class nLIBGEN:
    def __init__(self, bookPath, ebook_num, download_path):
        self.singsonglog = 'SingSongLog: '
        self.ebook_num = ebook_num
        self.booklist = self.readJson(bookPath)
        self.main_url = 'https://libgen.li/'
        self.query = 'index.php'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
            'Connection': 'keep-alive',
            'Host': 'libgen.li',
            'referer': 'https://libgen.li',
        }
        self.get_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
        }
        self.download_php = 'ads.php'
        self.get_php = 'get.php'
        self.verify = True
        # download_path in view of this: C:/Users/Lenovo/Desktop/ or just ''(null string)
        self.download_path = download_path

    def readJson(self, path):
        with open(path, 'r', encoding='utf-8') as pf:
            print(self.singsonglog + 'to download book list json file load successfully')
            return json.loads(pf.read())

    def download(self, href, filekind, bcount, bindex):
        #
        download_req = requests.get(self.main_url + href, headers=self.headers, verify=self.verify)
        if download_req.status_code != 200:
            print(self.singsonglog + 'Book: {}, Book count: {}'.format(self.booklist[bindex],
                                                                       bcount) + ' download request failed, status code: {}'.format(
                download_req.status_code))
            return
        print(self.singsonglog + 'Book: {}, Book count count: {}'.format(self.booklist[bindex],
                                                                         bcount) + ' download request successfully, start to download')
        with open(self.download_path + self.booklist[bindex] + '{}.{}'.format(bcount, filekind), 'wb') as pf:
            pf.write(download_req.content)
        print(self.singsonglog + 'Book: ' + self.booklist[bindex] + ' Book count: {}'.format(
            bcount) + ' downloaded successfully')

    def scrapy(self, book_table, bookindex):
        bcount = 0
        for book in book_table:
            bcount += 1

            bookinfos = book.select('td')
            kindinfo = bookinfos[-2].text
            href = bookinfos[-1].select('a')[0]['href']

            get_req = requests.get(href, headers=self.get_headers, verify=self.verify)
            if get_req.status_code != 200:
                print(self.singsonglog + 'Book: {}, Book count: {}'.format(self.booklist[bookindex],
                                                                           bcount) + ' get request failed')
                continue
            print(self.singsonglog + 'Book: {}, Book count: {}'.format(self.booklist[bookindex],
                                                                       bcount) + ' get request successfully')
            get_soup = bs(get_req.text, 'lxml')
            get_href = get_soup.select('#main a')[0]['href']

            t = threading.Thread(target=lambda: self.download(get_href, kindinfo, bcount, bookindex))
            t.start()

    def run(self):
        bindex = -1
        for book in self.booklist:
            bindex += 1
            # book is a string
            book_params = {
                'req': book
            }
            book_req = requests.get(self.main_url + self.query, headers=self.headers, params=book_params,
                                    verify=self.verify)
            if book_req.status_code != 200:
                print(self.singsonglog + 'Book: ' + book + ' book request failed, status code: {}'.format(
                    book_req.status_code))
            print(self.singsonglog + 'Book: ' + book + ' book request successfully')
            book_soup = bs(book_req.text, 'lxml')
            book_table = book_soup.select('#tablelibgen tbody tr')
            del book_soup
            if len(book_table) == 0:
                print(self.singsonglog + 'Book: ' + book + ' not found in the website')
                continue
            t = threading.Thread(target=lambda: self.scrapy(book_table[0:self.ebook_num], bindex))
            t.start()


# booklist.json includes some book that in this format
# [
#     "Hello World", "coding", "百年孤独","我是猫","伊豆的舞女"
# ]
bookPath = "C:/Users/HUAWEI/Desktop/downloadbooklist.json"
ebook_num = 2
download_path = 'D:/DownloadBooks/'

libgen = nLIBGEN(bookPath, ebook_num, download_path)
libgen.run()
