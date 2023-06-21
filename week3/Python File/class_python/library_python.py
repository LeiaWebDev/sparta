
import requests # Requires installation of requests library

r = requests.get('http://spartacodingclub.shop/en/global_air/seoul')
rjson = r.json()

# print(rjson['data']['forecast'][0]['avg'])

days = rjson['data']['forecast']

for day in days:
    if day['avg'] < 100:
        print(day['day'], day['avg'])