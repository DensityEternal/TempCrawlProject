import re
from io import BytesIO

import ddddocr
import requests
from PIL import Image

targetUrl = 'http://ydjwxs.yzu.edu.cn/login'


def CaptchaRecognition(img):
    ocr = ddddocr.DdddOcr()
    captcha = ocr.classification(img)
    return captcha


headers = {'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding':
            'gzip, deflate',
        'Accept-Language':
            'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cookie':
            'JSESSIONID=aaaCF4Uvzg1oth04BViGy; ace_settings=%7B%22sidebar-collapsed%22%3A1%7D; selectionBar=82022',

        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "ydjwxs.yzu.edu.cn",
    "Referer": "http://ydjwxs.yzu.edu.cn/",
    "X-Requested-With": "XMLHttpRequest"
    }
cookie = {'cookie': 'JSESSIONID=aaaCF4Uvzg1oth04BViGy; ace_settings=%7B%22sidebar-collapsed%22%3A1%7D; selectionBar=82022',
}
response = requests.post(targetUrl, cookies=cookie, headers=head)
print(response.status_code)
print('Have been finished')
pattern = re.compile(r'id="captchaImg" src="(.*?)"')
imgPath = pattern.search(response.text)
imgPath = 'http://ydjwxs.yzu.edu.cn' + imgPath.group().split('src=')[-1].split('"')[-2]
p = re.compile(r'name="tokenValue" value="(.*?)"')
tokenValue = p.search(response.text)
tokenValue = tokenValue.group().split('value=')[-1].split('"')[-2]

req_captcha = requests.get(imgPath)
img = Image.open(BytesIO(req_captcha.content))
captchaValue = CaptchaRecognition(img)
print(captchaValue)
print('start now')
data = {
    "j_username": '211201109',
    "input_password": '211201109',
    "j_captcha": captchaValue,
    'tokenValue': tokenValue,
    'request': 'http://ydjwxs.yzu.edu.cn',
    "remainingTime ": ''
}
response = requests.post(targetUrl, data=data, headers=headers,timeout=5,stream=True)
print(response.status_code)
print(response.headers)
print(imgPath)
print(response.content.decode())
# print(response.text)
