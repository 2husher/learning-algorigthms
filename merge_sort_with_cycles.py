def merge_sort_with_cycles(data):
    data2 = []
    for x in data:
        data2.append([x])   # n
    data = data2
    is_sorted = False
    data2 = []
    while not is_sorted: # log n
        is_sorted = True
        while len(data) > 1:
            is_sorted = False
            first = data.pop()
            second = data.pop()
            merged = merge(first, second)   # n
            data2.append(merged)
        if len(data) == 1:
            last = data.pop()
            data2.append(last)
        data = data2
        data2 = []
    return data.pop()


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
    num = 50
    alist = []
    for i in range(num):
        elem = random.randint(0, 100)
        alist.append(elem)
    checked = sorted(alist)


    merge_sorted_with_cycles = merge_sort_with_cycles(alist.copy())
    # print(f"MERGE SORTED CYCLES: {merge_sorted_with_cycles}")
    assert merge_sorted_with_cycles == checked


main()
