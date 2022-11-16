#dumps method
import requests
import json

#python to json
data = { 
    'name':'Pro',
    'student_id' : '011151245',
    'year': 3,
    }

data = json.dumps(data)

print('data:',data)

#send as json
url = "http://127.0.0.1:8000/studentinfo/create/"

send_data = requests.post(url=url, data=data)
s_data = send_data.json()
print('send_data',s_data)
# #json to python

# file_name = 'Practises\json.txt'

# with open(file_name,'r',encoding='utf-8') as f:

#     data = json.load(f)

#     print(data)
#     print(data['name'])
#     print(data['id'])
#     print(data['year'])     

