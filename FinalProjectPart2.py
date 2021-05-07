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

for x in range(0, len(list1)):
    list1[x][3] = int(list1[x][3])


def bubble_sort(sort_list):
    for j in range(len(sort_list) - 1, 0, -1):
        for k in range(j):
            if sort_list[k][3] < sort_list[k + 1][3]:
                m = sort_list[k]
                sort_list[k] = sort_list[k + 1]
                sort_list[k + 1] = m


bubble_sort(list1)
while 1:
    input1 = str(input("Enter item manufacturer and type:"))
    if input1 == 'q':
        break
    else:
        item = []
        similar_item = []
        input1 = input1.split()
        for a in range(0, len(list1)):
            if len(input1) == 2:
                if input1[1] in list1[a][2]:
                    current_date = datetime.now().date()
                    date = list1[a][4]
                    date2 = datetime.strptime(date, "%m/%d/%Y").date()
                    past_date = date2 < current_date
                    if input1[0] in list1[a][1]:
                        if not past_date and list1[a][5] != "damaged":
                            item.append(list1[a])
                    else:
                        if not past_date and list1[a][5] != "damaged":
                            similar_item.append(list1[a])
            if len(input1) == 3:
                if input1[2] in list1[a][2]:
                    current_date = datetime.now().date()
                    date = list1[a][4]
                    date2 = datetime.strptime(date, "%m/%d/%Y").date()
                    past_date = date2 < current_date
                    if input1[1] in list1[a][1]:
                        if not past_date and list1[a][5] != "damaged":
                            item.append(list1[a])
                    else:
                        if not past_date and list1[a][5] != "damaged":
                            similar_item.append(list1[a])
        diff = []
        if len(item) == 0:
            print("No such inventory")
        elif len(item) != 0:
            for b in range(0, 1):
                print("Your item is: 'ID': {}, 'Manufacturer': {}, 'Type': {}, 'Price': {}".format
                      (item[b][0], item[b][1], item[b][2], item[b][3]))
                if len(item) != 0 and len(similar_item) != 0:
                    for c in range(0, len(similar_item)):
                        diff.append(similar_item[c][3])


                    def nearest_value(values, one):
                        closest = None
                        closest_dist = None
                        for v in values:
                            dist = abs(v - one)
                            if closest_dist is None or dist < closest_dist:
                                closest = v
                                closest_dist = dist
                            elif dist == closest_dist:
                                closest = min(v, closest)
                        return closest


                    close = nearest_value(diff, item[b][3])
                    for d in range(0, len(similar_item)):
                        if close == similar_item[d][3]:
                            print("You may, also consider: 'ID': {}, 'Manufacturer': {}, 'Type': {}, 'Price': {}"
                                  .format(similar_item[d][0], similar_item[d][1],
                                          similar_item[d][2], similar_item[d][3]))
