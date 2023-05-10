from dllists import *

def merge_sort_ddlist(dllist):
    if dllist.count() < 2:
        # print(f"{data}")
        return dllist

    k = dllist.count() // 2

    left = DoubleLinkedList()
    right = DoubleLinkedList()
    for i in range(0, dllist.count()):
        elem = dllist.unshift()
        if i < k:
            left.push(elem)
        else:
            right.push(elem)

    # print(f"LEFT {left}, RIGHT: {right}")
    left = merge_sort_ddlist(left)
    right = merge_sort_ddlist(right)

    # print(f"MERGE: LEFT {left}, RIGHT: {right}")
    dllist = merge_ddlist(left, right)
    return dllist


def merge_ddlist(left, right):
    dllist = DoubleLinkedList()

    while left.count() > 0 and right.count() > 0:
        if left.first() < right.first():
            elem = left.unshift()
            dllist.push(elem)
        else:
            elem = right.unshift()
            dllist.push(elem)

    while left.count() > 0:
        elem = left.unshift()
        dllist.push(elem)

    while right.count() > 0:
        elem = right.unshift()
        dllist.push(elem)

    return dllist


import random


def main_dllist():
    num = 30
    dllist = DoubleLinkedList()
    for i in range(num):
        elem = random.randint(0, 10000)
        dllist.push(elem)

    dllist_sorted = merge_sort_ddlist(dllist)
    print("SORTED DLLIST:", end = " ")
    print_dllist(dllist_sorted)
    print("END")
    assert is_sorted(dllist_sorted)


def is_sorted(dllist):
    elem = dllist.first()
    for i in range(1, dllist.count()):
        next_elem = dllist.get(i)
        # print(f"i: {i} ELEM: {elem} NEXT_ELEM: {next_elem}")
        if elem > next_elem:
            return False
        elem = next_elem
    return True


def print_dllist(dllist):
    for i in range(dllist.count()):
        print(dllist.get(i), end = " ")


main_dllist()
