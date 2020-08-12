import requests


city = input('City?\n')
api_url = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    'q': city,
    'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
    'units': 'metric'
}

response = requests.get(api_url, params=params)

data = response.json()
for i in data:
    print(i, data[i])

print('Temp in ', city, ' is ', data['main']['temp'])
