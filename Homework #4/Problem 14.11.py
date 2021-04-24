# Madison Fletcher
# 1868748
def selection_sort_descend_trace(num):
    length = len(num)
    for i in range(length-1):
        k = i
        for j in range(i + 1, length):
            if num[j] > num[k]:
                k = j
        num[i], num[k] = num[k], num[i]
        print(' '.join([str(x) for x in num]), '')
    return num


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)
