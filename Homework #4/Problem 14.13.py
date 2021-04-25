# Madison Fletcher
# 1868748
num_calls = 0


def partition(user_ids, i, k):
    pivot = user_ids[(i + k) // 2]
    while i <= k:
        while user_ids[i] < pivot:
            i = i + 1
        while user_ids[k] > pivot:
            k = k - 1
        if i <= k:
            y = user_ids[i]
            user_ids[i] = user_ids[k]
            user_ids[k] = y
            i = i + 1
            k = k - 1
    return i


def quicksort(user_ids, i, k):
    global num_calls
    num_calls = num_calls + 1
    if i >= k:
        return user_ids
    p = partition(user_ids, i, k)
    quicksort(user_ids, i, p - 1)
    quicksort(user_ids, p, k)


if __name__ == "__main__":
    user_ids2 = []
    user_id = input()
    while user_id != "-1":
        user_ids2.append(user_id)
        user_id = input()

    quicksort(user_ids2, 0, len(user_ids2) - 1)

    print(num_calls)

    for user_id in user_ids2:
        print(user_id)
