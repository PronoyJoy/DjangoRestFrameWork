import requests
import json

url = "http://127.0.0.1:8000/studentinfo/student/"

def get_data(student_id = None):
    data ={}
    if student_id is not None:
        data = {'student_id':student_id}

    json_data = json.dumps(data)
    read = requests.get(url = url, data = json_data)
    data = read.json()
    print(data)

#get_data('1')

def post_data():
    data ={
        'name' : 'sohag',
        'student_id' : '5',
        'year' : 4
    }

    json_data = json.dumps(data)
    response = requests.post(url=url, data = json_data)
    json_data = response.json()
    print(json_data)
post_data()