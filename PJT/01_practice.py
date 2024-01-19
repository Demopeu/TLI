import requests

url =  'https://fakestoreapi.com/carts'
data = requests.get(url).json()
print(data)
