import csv

datas = open('linksExtraidos26.csv')

linhas = csv.reader(datas)
data_lista = []

for data in datas:
    data_lista.append(data)

data_set = set(data_lista)

print(len(data_lista))
print(len(data_set))

data_dict = {}

for item in data_lista:
    if item in data_dict.keys():
        data_dict[item] += 1
    else:
        data_dict[item] = 1

for item in data_dict:
    if data_dict[item] > 1:
        print(item)
        print(data_dict[item])

print(data_dict)
