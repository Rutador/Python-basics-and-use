import os
import os.path
import zipfile

os.chdir('c:/')
print(os.listdir())

f = zipfile.ZipFile('main.zip', 'r')
f.extractall()
f.close()

ans_list = []
for i, k, l in os.walk('main'):
    print(i, k, l)
    for j in l:
        if (j[-3:] == '.py') and (i not in ans_list):
            ans_list.append(i)

ans_list.sort()
print(ans_list)

os.chdir('Users\\user\\dev\\Курс Python - основы и применение\\2_4 File sistem and files\\task2')
print(os.listdir())
with open('answer', 'w') as output:
    for i in ans_list:
        output.write(i + '\n')
