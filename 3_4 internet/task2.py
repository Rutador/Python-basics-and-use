import requests
import re

link = 'http://pastebin.com/raw/7543p0ns'
a = requests.get(link)
domains = re.findall(r"""<a.*href=['"][fhtps]{0,5}[:/]*(\w[a-zA-Z0-9.-]*)""", a.text)
domains = list(set(domains))
for i in sorted(domains):
    print(i)
