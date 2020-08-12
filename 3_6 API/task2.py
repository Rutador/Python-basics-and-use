import requests
import json

data_base = []
client_id = '2c3e7b46480cfde24db5'
client_secret = '109bf0bc21498512f3ae1194efdd17ef'
r = requests.post('https://api.artsy.net/api/tokens/xapp_token',
                  data={'client_id': client_id,
                        'client_secret': client_secret
                  })
j = json.loads(r.text)
token = j['token']
headers = {'X-Xapp-Token': token}

with open('dataset_24476_4.txt') as inf:
    for line in inf:
        artist_id = line.strip()
        response = requests.get('https://api.artsy.net/api/artists/' + artist_id, headers=headers)
        artist_data = json.loads(response.text)
        name = artist_data['sortable_name']
        birth = str(artist_data['birthday'])
        data_base.append(birth + name)

data_base.sort()
for i in data_base:
    print(i[4:])
