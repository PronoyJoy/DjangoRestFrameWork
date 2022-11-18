import requests
import json

url = "http://127.0.0.1:8000/studentinfo/updatedelete/"

def delete_data(student_id):
    data = {
        'student_id' : student_id,
    }
    json_data = json.dumps(data)
    response = requests.delete(url=url, data = json_data)
    data = response.json()
    print(data)

delete_data('5')