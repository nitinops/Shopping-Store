import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos"
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, headers=headers)
response.json()
