import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos"
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
response.json()
