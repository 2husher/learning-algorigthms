def merge_sort(data):
    if len(data) < 2:
        return data

    k = len(data) // 2
    left = data[:k]
    right = data[k:]
    left = merge_sort(left)
    right = merge_sort(right)

    data = merge(left, right)
    return data


def merge(left, right):
    data = []
    while left != [] and right != []:
        if left[0] < right[0]:
            data.append(left[0])
            left = left[1:]
        else:
            data.append(right[0])
            right = right[1:]

    if left != []: data += left # data.extend(left)
    if right != []: data += right # data.extend(right)
    return data


import random


def main():
    num = 30
    alist = []
    for i in range(30):
        elem = random.randint(0, 10000)
        alist.append(elem)
    merge_sorted = merge_sort(alist)
    checked = sorted(alist)
    assert merge_sorted == checked
    print(f"MERGE SORTED: {merge_sorted}")


main()
