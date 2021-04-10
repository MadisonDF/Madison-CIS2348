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

# while loop will create a new file for each item type until the user gives a blank input.
while True:
    type_list1 = str(input("Enter item type:"))
    for a in range(0, len(list1)):
        if list1[a][2] == type_list1:
            count = list1[a][2].count(type_list1)
            if count == 1:
                cap = type_list1.capitalize()
                type_file1 = cap + "Inventory.csv"
                full_inv = open(type_file1, 'w', newline='')
                w_file = csv.writer(full_inv)
                for c in range(0, len(list1)):
                    list1.sort()
                    if list1[c][2] == type_list1:
                        w_file.writerow(list1[c])
    if type_list1 == "":
        break
