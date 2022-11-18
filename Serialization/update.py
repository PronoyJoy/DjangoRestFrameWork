import requests
import json

url = "http://127.0.0.1:8000/studentinfo/update/"

def update_data():
    data = {
        'name' : 'Pronoy',
        'student_id' : '2',
        'year' :7
    }
    json_data = json.dumps(data)
    response = requests.put(url=url, data = json_data)
    data = response.json()
    print(data)

update_data()