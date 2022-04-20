import re
import requests
import json
from bs4 import BeautifulSoup
from xpinyin import Pinyin


# 天气
# url = 'http://apis.juhe.cn/simpleWeather/query'
# params = {
#     'city': '合肥',
#     'key': '8539018f9e6fd36fe42780398a59ec41'
# }
# response = requests.get(url=url, params=params)
# result = response.json()
# with open('weather.json', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(result, indent=2, ensure_ascii=False))

# 生活指数
# url = 'http://apis.juhe.cn/simpleWeather/life'
# params = {
#     'city': '合肥',
#     'key': '8539018f9e6fd36fe42780398a59ec41'
# }
# response = requests.get(url=url, params=params)
# result = response.json()
# with open('living_index.json', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(result, indent=2, ensure_ascii=False))

# pm2.5
# base_url = 'https://pm25.im/'
# city = '合肥'
# p = Pinyin()
# url = base_url + p.get_pinyin(city).replace('-', '') + '/'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# response = requests.get(url=url, headers=headers)
# soup = BeautifulSoup(response.text, 'lxml')
# # p = soup.find(name='p', attrs={'class': 'denseness'}).contents[-3::2]
# text = soup.find(name='p', attrs={'class': 'denseness'}).text
# print(text)
# values = []
# for _, pm in enumerate(p):
#     values.append(re.findall('\d+', pm)[0])
# keys = ['PM2.5', 'PM10']
# result = dict(zip(keys, values))
# print(result)

# url = 'https://devapi.qweather.com/v7/air/now?location=101010100&key=8e54dd30c3f2413f8c5002d067b932ed'
url = 'https://devapi.qweather.com/v7/air/now'
params = {
    'location': '101010100',
    'key': '8e54dd30c3f2413f8c5002d067b932ed'
}
response = requests.get(url, params=params)
print(response.json())

# url = 'https://devapi.qweather.com/v7/weather/3d'
# response = requests.get(url=url, params=params)
# print(response.json())

# url = 'https://devapi.qweather.com/v7/indices/1d'
# params = {
#     'type': '0',
#     'location': '101010100',
#     'key': '8e54dd30c3f2413f8c5002d067b932ed'
# }
# response = requests.get(url=url, params=params)
# print(response.json())



