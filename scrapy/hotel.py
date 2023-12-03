import re
import requests
import time
import os
TargetUrl = "https://www.bilibili.com/"
headers={
    "Host":TargetUrl,
    "X-Requested-With":'XMLHttpRequest',
    'user-agent':'Requested-With,If-Modified-Since,Pragma,Last-Modified,Cache-Control,Expires,Content-Type,Access-Control-Allow-Credentials',
    'cookie':'innersign=0; buvid3=15EE7E18-87B3-BF02-8653-8F6964563AE739183infoc; b_nut=1697353739; i-wanna-go-back=-1; b_ut=7; b_lsid=1037AE151_18B322AAC15; _uuid=1049779C7-1010102-83CD-4181-4AED3A33415D39293infoc; enable_web_push=DISABLE; buvid_fp=ec5e4bd4d25854edaafc20d78cb1b52b; buvid4=8EA23C9C-488F-5CC5-9B48-D3EC8857DD7471807-023100622-7XDfT9HnZ75LXiTdE8NLAa6P5th9F4rNkOE370QxcXeVTASwi1w2Ow%3D%3D; SESSDATA=e6da43b3%2C1712905763%2Caf75d%2Aa2CjCpq7WMPI2QI4UGkHxXE0iVzclFoto0nq-Xi7IcgElZ4XpVPV44GShlUGTJfKTswhYSVlMxUXFZV0lERG9PbldUaDhlbGpSMlhPUHl5RXdRQ0o4WVVldG5IeUtONDFWaXNZUHN4blBPS19DOXViT1NYZS1TbTNYV1V1aXdEWUZpSGhJdElFRkFnIIEC; bili_jct=bb49f68dcd92355637a10be169e9b7ed; DedeUserID=343958045; DedeUserID__ckMd5=931d046c2f321277; CURRENT_FNVAL=4048; sid=7ksz7u30; PVID=1; header_theme_version=CLOSE; home_feed_column=4; browser_resolution=366-883'}
pattern=re.compile('<div class="feed-card" data-v-6bc13a14>(.*?)</div>')
response=requests.get(TargetUrl,headers=headers)
imgUrl=[]
print(pattern.search(response.text))
print(response.status_code)
with open('temp.txt','wb')as temp:
    temp.write(response.content)