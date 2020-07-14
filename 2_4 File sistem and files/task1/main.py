
temp_list = []

with open('dataset_24465_4.txt', 'r') as source, open('to.txt', 'a') as dest:
    for i in source:
        temp_list.append(i)
    print(temp_list)
    for i in range(len(temp_list) - 1, -1, -1):
        dest.write(temp_list[i])
