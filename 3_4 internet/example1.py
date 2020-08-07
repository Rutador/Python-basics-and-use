import requests

a = requests.get('https://docs.python.org/3.5')
print(a.status_code)
for i in a.headers:
    print(i, ' - ', a.headers[i])
print(type(a))
print(a.text)
