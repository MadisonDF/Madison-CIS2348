# Madison Fletcher
# 1868748
import csv
filename = input()
file = open(filename, 'r')
reader = csv.reader(file, delimiter=',')
count = {}
for line in reader:
    for word in line:
        if word in count.keys():
            count[word] = count[word] + 1
        else:
            count[word] = 1
for x in count:
    print(x, count[x])
