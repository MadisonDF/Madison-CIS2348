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


def bubble_sort(sort_list):
    n = len(sort_list)
    for j in range(0, n):
        for k in range(0, n - j - 1):
            if sort_list[k][1] > sort_list[k + 1][1]:
                b = sort_list[k]
                sort_list[k] = sort_list[k + 1]
                sort_list[k + 1] = b
    return sort_list


bubble_sort(list1)

full_inv = open("FullInventory.csv", 'w', newline='')
w_file = csv.writer(full_inv)
for a in range(0, len(list1)):
    w_file.writerow(list1[a])
