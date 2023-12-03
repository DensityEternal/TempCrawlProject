import json
import re
import threading

import requests


class nSHIYINREN:
    def __init__(self, path, download_path):
        self.singsonglog = 'SingSongLog: '
        self.path = path
        self.download_path = download_path
        # musiclist is a list of music name in array view
        self.musiclist = self.readJson()
        self.rs_url = 'http://search.kuwo.cn/r.s'
        self.json_url = 'http://json.170hi.com/api/v1/www/music/playUrl'
        self.json_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0",
            "Host": "www.shiyinren.com",
            "Connection": "keep-alive",
            "Referer": "https://www.kuwo.cn/",
            "Host": "search.kuwo.cn",
            "Origin": "https://www.kuwo.cn/"
        }
        self.download_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0',
            'Host': 'sr-sycdn.kuwo.cn',
            'Connection': 'keep-alive',
        }
        self.url_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0',
            'Referer': 'http://www.shiyinren.com',
        }

        self.verify = True

    def readJson(self):
        with open(self.path, 'r', encoding='utf-8') as pf:
            print(self.singsonglog + 'musiclist reading...')
            return json.loads(pf.read())

    def download(self, url, songName):
        download_req = requests.get(url, headers=self.download_headers, verify=self.verify)
        headers = self.download_headers
        headers['Referer'] = url
        if download_req.status_code != 200:
            print(self.singsonglog + songName + ' download request failed, status code: {}'.format(
                download_req.status_code))
            return
        with open(self.download_path + songName + '.mp3', 'wb') as pf:
            pf.write(download_req.content)
        print(self.singsonglog + songName + '.mp3 downloaded in path: ' + self.download_path)

    def run(self):
        for music in self.musiclist:
            params = {
                'all': music,
                'ft': 'music',
                'client': 'kt',
                'cluster': '0',
                'rn': '10',
                'rformat': 'json',
                'callback': 'searchMusicResult',
                'encoding': 'utf8',
                'vipver': 'MUSIC_8.0.3.1'
            }
            json_req = requests.get(self.rs_url, params=params, headers=self.json_headers, verify=self.verify)
            if json_req.status_code != 200:
                print(self.singsonglog + 'json request failed, status code: {}'.format(json_req.status_code))
                continue
            print(self.singsonglog + 'json request successfully')
            js = json_req.text
            match = re.search(r'(?<=MUSIC_)(\d+)', js)

            if not match:
                print(self.singsonglog + 'music id not found')
                continue
            id = match.group(1)
            del json_req
            del js
            del match

            params = {
                'mid': id,
                'type': 'convert_url',
                'br': '320kmp3'
            }
            url_req = requests.get(self.json_url, params=params, headers=self.url_headers, verify=self.verify)
            if url_req.status_code != 200:
                print(self.singsonglog + 'url request failed, status code: {}'.format(url_req.status_code))
                continue
            print(self.singsonglog + 'url request successfully')
            url = (json.loads(url_req.text))['data']['url']
            print(self.singsonglog + 'song: ' + music + ' url: ' + url)
            del params
            del url_req

            threading.Thread(target=lambda: self.download(url, music)).start()


musiclist_path = "C:/Users/HUAWEI/Desktop/downloadMusic.json"
download_path = "C:/Users/HUAWEI/Desktop/NewFolder/Music/"

shiyinren = nSHIYINREN(musiclist_path, download_path)
shiyinren.run()
