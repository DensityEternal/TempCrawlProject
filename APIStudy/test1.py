import json
import requests
"""
    在这个项目里，按着步骤操作，咦？结果发现丢出个error，最后发现是要我绑卡，奈何囊中羞涩，无法满足这个需求
"""
API_KEY = 'AIzaSyCvvnBBzGJZDjqlHZxmNO4AreaNOJ7ODOk'


def getGo(add):
    add = str(add).replace('', '+')
    query = \
        'https://maps.googleapis.com/maps/api/geocode/' \
        'json?address={}&key={}' \
            .format(add,API_KEY)
    response = requests.get(query)
    j = json.loads(response.text)
    return j.get('results')[0].get('geometry').get('viewport').get('southwest').values()


def getTimeZone(val1, val2):
    query = \
        'https://maps.googleapis.com/maps/api/timezone/json?loaction={},{}&timestamp=1412649030&key={}'. \
            format(val1, val2, API_KEY)
    response = requests.get(query)
    j = json.loads(response.text)
    print(j)
    return j.get("timeZoneName"), j.get('timeZoneId')


if __name__ == '__main__':
    print(getTimeZone(34.18, 100.65))
    address = input('please input address:')
    q = list(getGo(address))
    print(getTimeZone(q[0], q[1]))
