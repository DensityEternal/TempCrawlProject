import urllib
from urllib import parse
from urllib.request import Request, urlopen

import ddddocr
from PIL import Image

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

captchaurl = r'http://ydjwxs.yzu.edu.cn/img/captcha.jpg'
req_captcha=Request(captchaurl,headers=head)
response_captcha=urlopen(req_captcha)
img=Image.open(response_captcha)
def CaptchaRecognition(img):
    ocr = ddddocr.DdddOcr()
    captcha = ocr.classification(img)
    return captcha
captchaValue=CaptchaRecognition(img)
web_url = 'http://ydjwxs.yzu.edu.cn/login'
params = {
    "j_username": '211201109',
    "input_password": '211201109',
    "return_url": 'http://ydjwxs.yzu.edu.cn',
    '_post_type': 'ajax',
    "j_captcha":captchaValue
}
data = bytes(urllib.parse.urlencode(params), 'utf-8')
req = Request(web_url, headers=head, data=data, method='POST')
response = urlopen(req)


img=Image.open(response)
print(response.read().decode('utf-8'))


