import requests

heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'user': '444896474',
    'passwd': '635089018',


}
targetUrl = r'https://seer.61.com/events/2023return/'


payload = {'user': '444896474',
           'passwd': '635089018',
           'cookie':'TMACMAIN_V3=sk4dttr557mhvv6j0iimso0ku8; PHPSESSID=pic6k04kplj8pi8gbjb161bo6b'
           }
session=requests.Session()

response=requests.get(targetUrl,data=payload,headers=heads)
print(response.status_code)
print(response.text)
print()
cookie={
    'PHPSESSID':'imb83cl5vqqi3kdm4docffri44',
    'TMACMAIN_V3':'irg37itpjnkqg7tf5o32d7kii2',
    'tm-uuid':'01745fc2-be74-21e9-01b3-d1d51f304d2b',
    'ab_sr':'1.0.1_N2FmNzAwZTYzMjU2ODRmMTY2NmNhZmMwMDQ2OTdlZTFhZWVjYzQyMTM4MThjMjI2MDIzOWMyMzdhNTJmM2UyN2JkYjU3ZTk0Y2I4NjExMGQyM2E2ZmRlNDMyMTkxYzdlY2EzOGJkNzYwYzk3ZGNiNzZmNTBhNDUwYzM5MjUyYTZhMDA5MGQxYzI1M2VkMDNiNGFjNWY1MjcxYWEyN2NkZjA3MmM0NWRiNDc4MmIyZGYyYzM1N2M2NjQ3ZmFlNjU0MzIzZTFmYjhiMmNlNmJjMDllMzJiNTYwNThhYmJiZDk='

}
response=session.get(targetUrl,cookies=cookie)
print(response.status_code)



