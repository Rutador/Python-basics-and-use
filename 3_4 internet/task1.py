import requests
import re

str1 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
str2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
flag = False

a = requests.get(str1)
links = re.findall(r'<a href="(.+)">', a.text)
# print(a.text)
# print(links)
for link in links:
    b = requests.get(link)
    # print('b.text: \n', b.text)
    if str2 in re.findall(r'<a href="(.+)">', b.text):
        flag = True
        break
print('Yes' if flag else 'No')
