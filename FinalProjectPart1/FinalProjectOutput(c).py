# Madison Fletcher
# 1868748
import csv
from datetime import datetime
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

list1.sort(key=lambda elem: elem[4])

service_inv = open("PastServiceDateInventory.csv", 'w', newline='')
w_file = csv.writer(service_inv)
for a in range(0, len(list1)):
    current_date = datetime.now().date()
    date = list1[a][4]
    date2 = datetime.strptime(date, "%m/%d/%Y").date()
    if date2 < current_date:
        w_file.writerow(list1[a])
