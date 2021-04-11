# Madison Fletcher
# 1868748
import csv
list1 = []
list2 = []
list3 = []

filename = "ManufacturerList.csv"
file = open(filename, 'r')
reader = csv.reader(file)
for x in reader:
    list1.append(x)
    list1.sort()

filename2 = "PriceList.csv"
file2 = open(filename2, 'r')
reader2 = csv.reader(file2)
for y in reader2:
    list2.append(y)
    list2.sort()

filename3 = "ServiceDatesList.csv"
file3 = open(filename3, 'r')
reader3 = csv.reader(file3)
for z in reader3:
    list3.append(z)
    list3.sort()


for i in range(len(list1)):
    list1[i].insert(len(list1[i]) - 1, list2[i][1])
    list1[i].insert(len(list1[i]) - 1, list3[i][1])

for m in range(0, len(list1)):
    list1[m][3] = int(list1[m][3])


def bubble_sort(sort_list):
    for j in range(len(sort_list) - 1, 0, -1):
        for k in range(j):
            if sort_list[k][3] < sort_list[k + 1][3]:
                b = sort_list[k]
                sort_list[k] = sort_list[k + 1]
                sort_list[k + 1] = b


bubble_sort(list1)
print(list1)
damage_inv = open("DamagedInventory.csv", 'w', newline='')
w_file = csv.writer(damage_inv)
for a in range(0, len(list1)):
    if list1[a][5] == "damaged":
        print(list1[a])
