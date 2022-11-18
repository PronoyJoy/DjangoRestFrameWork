import requests

url = requests.get(url='http://127.0.0.1:8000/studentinfo/list/')

data = url.json()

print(data)