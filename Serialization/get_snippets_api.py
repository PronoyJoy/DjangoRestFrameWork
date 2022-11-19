import requests
import json

url = "http://127.0.0.1:8000/studentinfo/snippet/"

def get_data(title = None):
    data ={}
    if title is not None:
        data = {'title': title}

    json_data = json.dumps(data)
    read = requests.get(url = url, data = json_data)
    data = read.json()
    print(data)

get_data()
