import csv

crimes = []
crimes_numbers = {}
with open('Crimes.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        if ('2015' in row[2]) and (row[5] in crimes_numbers):
            print('ok')
            crimes_numbers[row[5]] = crimes_numbers[row[5]] + 1
        elif '2015' in row[2]:
            crimes_numbers.update({row[5]: 1})

print(crimes_numbers)
max_num = ['something', 0]
for i, k in crimes_numbers.items():
    if k > max_num[1]:
        max_num = [i, k]
print(max_num)
