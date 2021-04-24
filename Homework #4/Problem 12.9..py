# Madison Fletcher
# 1868748
list1 = []
while 1:
    x = input().split()
    if x[0] == "-1":
        break
    try:
        list1.append([x[0], int(x[1]) + 1])
    except ValueError:
        list1.append([x[0], 0])
for x, y in list1:
    print(x, y)
