#dumps method

import json

#python to json
data = { 
    'name':'Pronoy',
    'id' : '011151242',
    'year': 3,
    }

data = json.dumps(data)

print('data:',data)


#json to python

file_name = 'Practises\json.txt'

with open(file_name,'r',encoding='utf-8') as f:

    data = json.load(f)

    print(data)
    print(data['name'])
    print(data['id'])
    print(data['year'])     

