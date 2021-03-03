# Madison Fletcher
# 1868748
import csv
filename = input()
file = open(filename, 'r')
reader = csv.reader(file, delimiter=',')
count = []
for line in reader:
    word = set(line)
    for x in word:
        count = line.count(x)
        print(x, count)
