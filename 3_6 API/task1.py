import requests

with open('dataset_24476_3.txt') as inf:
    for line in inf:
        num = line.strip()
        api_url = 'http://numbersapi.com/'+num+'/math?json'

        response = requests.get(api_url)

        data = response.json()
        print('Interesting' if data['found'] else 'Boring')
