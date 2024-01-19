import requests
from pprint import pprint as pp

# url =  'https://fakestoreapi.com/carts'
# data = requests.get(url).json()
# print(data)

api_key = '9ddbf62848dbb7c41c4fbe8a883d4e46'
# api_key = '87246d75e1ce26e1392a087b3d1d88c5'
lat = 37.56
lon = 126.97

url =  f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
data = requests.get(url).json()

pp(data.keys())
# 날씨 요약 정보: 서울 기준 'clear sky'가 되도록 출력해 보자!
# pp(data['weather'][0]['description'])

# 추가 공부 과제

# data['weather']
# data.get['weather']

