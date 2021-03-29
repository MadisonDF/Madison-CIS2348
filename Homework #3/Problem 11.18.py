# Madison Fletcher
# 1868748
list1 = []
number = input()
list_num = number.split()
for i in range(len(list_num)):
    num = int(list_num[i])
    if num >= 0:
        list1.append(num)
list1.sort()
list2 = str(list1)[1:-1]
list3 = list2.replace(',', '')
print(list3, end=' ')
