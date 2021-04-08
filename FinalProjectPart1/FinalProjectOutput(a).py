# Madison Fletcher
# 1868748
import copy
import csv

list1 = []
list2 = []
list3 = []

filename = str(input())
file = open(filename, 'r')
reader = csv.reader(file)
for x in reader:
    list1.append(x)

filename2 = str(input())
file2 = open(filename2, 'r')
reader2 = csv.reader(file2)
for y in reader2:
    list2.append(y)

filename3 = str(input())
file3 = open(filename3, 'r')
reader3 = csv.reader(file3)
for z in reader3:
    list3.append(z)

new_list = copy.deepcopy(list1)
for x in range(0, len(list1)):
    new_list[x].remove(list1[x][-1])

for x in range(0, len(list1)):
    new_list[x].append(list2[x][1])

for x in range(0, len(list1)):
    new_list[x].append(list3[x][1])

for x in range(0, len(list1)):
    new_list[x].append(list1[x][-1])

list1.sort(key=lambda elem: elem[1])
print()
full_inv = open("FullInventory.csv", 'w', newline='')
full_write = csv.writer(full_inv)
for x in range(0, len(list1)):
    full_write.writerow(list1[x])
