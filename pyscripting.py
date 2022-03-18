import requests
import json
response_API = requests.get('https://fakestoreapi.com/products')
data = response_API.text
print(data)
