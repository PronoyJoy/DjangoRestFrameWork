import requests,json

url = "http://127.0.0.1:8000/studentinfo/snippet/"

def post_data():
    data ={
        'title': 'rt',#object level validation error
        'code' : 'a= 6 b=7 print(a-b)',
        'linenos': True,
        'language':'javascript',
        'style' : 'igor'

    }

    json_data = json.dumps(data)
    response = requests.post(url=url, data = json_data)
    json_data = response.json()
    print(json_data)
post_data()