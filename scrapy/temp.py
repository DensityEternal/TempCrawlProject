import re

from requests import Session
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
targetUrl = r'https://zhenti.burningvocabulary.com/cet6/2023-06/01'
url = r'https://zhenti.burningvocabulary.com/cet6'
heads = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection':
        'keep-alive',
    'Cookie':
        'https_waf_cookie=520e7c73-1909-46c8cb57e2970713d7281eb13f5d421c9790; _cuid=83d14317-544c-48a8-a484-37f2fac57301__1698209299794',
    'Host': 'zhenti.burningvocabulary.com',
    'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform':
        'Windows',
    'Sec-Fetch-Dest':
        'document',
    'Sec-Fetch-Mode':
        'navigate',
    'Sec-Fetch-Site':
        'same-origin',
    'Sec-Fetch-User':
        '?1',
    'Upgrade-Insecure-Requests':
        '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36', }
data = {
    "botton_click": "answer_btn has"
}

session = Session()
html = session.get(url, headers=heads)

pattern = re.compile('<div class="(.*?)" title="查答案">查答案</div>')
chrome.get(targetUrl)
try:
    button = chrome.find_elements(By.TAG_NAME,'div').__dict__
    print(button)
except:
    source = session.get(targetUrl)
    print(source.status_code)
    print(source.text)

    button = pattern.search(source.text)
    print(button)
# response = requests.Request('post',targetUrl,headers=heads,data=data)
# prepared = response.prepare()
# prepared.body = prepared.body.replace("<div class='answer_container'></div>", "<div class='answer_container fadeIn'></div>")
# response = requests.Session().send(prepared)
# pattern = re.compile('class="answer_container fadeIn "')
# if response.status_code==200:
#     text = pattern.search(response.text)
#     if text:
#         print(text.group())
#     else:
#         print('Pattern not found in the response')
# else:
#     print('Fail to access in this site!')
#     print()
#     print(response.text)
