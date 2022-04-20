from urllib import response
import requests

url = 'https://geoapi.qweather.com/v2/city/lookup'
params = {
    'location': '合肥',
    'key': '8e54dd30c3f2413f8c5002d067b932ed'
}
response = requests.get(url=url, params=params)
print(isinstance(response.json()['location'][0]['id'], str))