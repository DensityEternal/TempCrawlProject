import re

import requests

session = requests.Session()
loginUrl = 'https://sso.yzu.edu.cn/login?service=http:%2F%2Feol.yzu.edu.cn%2Fmeol%2Fhomepage%2Fcommon%2Fsso_login.jsp'
targetUrl = 'http://eol.yzu.edu.cn/meol/personal.do'
data = {
    'username': '211201109',
    'password': 'pyf635089018666',
}

response = session.post(loginUrl,data=data)
cookie = {
    'cookie': 'JSESSIONID=7020C3E2B15C42718C495A5847E5881D; Hm_lvt_f0c0175943cff889a04ff6ae1368a90c=1697189195; Hm_lpvt_f0c0175943cff889a04ff6ae1368a90c=1697203633'}

head = {
    'referrer': 'http://eol.yzu.edu.cn/meol/popups/viewstudent_info.jsp?SID=190061&from=welcomepage',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'cookie': 'JSESSIONID=8FFCDDB052654779DA0150BF871ED5FE; Hm_lvt_f0c0175943cff889a04ff6ae1368a90c=1697189195,1697244583; Hm_lpvt_f0c0175943cff889a04ff6ae1368a90c=1697244636'
}

if response.status_code == 200:
    print('Successfully login!')
    try:
        response = session.get(targetUrl, headers=head)
        if response.status_code == 200:
            print('Successfully Logining!')
    except:
        print('Connection error!')
else:
    print('fail to login')
pattern = re.compile('class="info chgright".+')

name = pattern.search(response.text)
print(name)
