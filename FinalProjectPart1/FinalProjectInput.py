# Madison Fletcher
# 1868748
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