import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers = {"Content-Type":"application/json"}
response = requests.put(api_url, json=todo)
print(response.todo())




