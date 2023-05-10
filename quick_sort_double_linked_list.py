from dllists import *


def quick_sort_dllist(dllist):
    if dllist.count() < 2: return dllist

    middle_index = dllist.count() // 2
    middle_elem = dllist.get(middle_index)

    left = DoubleLinkedList()
    middle = DoubleLinkedList()
    right = DoubleLinkedList()

    while dllist.count() > 0:
        elem = dllist.unshift()
        if elem < middle_elem:
            left.push(elem)
        elif elem > middle_elem:
            right.push(elem)
        else:
            middle.push(elem)

    sorted_left = quick_sort_dllist(left)
    sorted_right = quick_sort_dllist(right)

    sorted_sequence = DoubleLinkedList()

    while sorted_left.count() > 0:
        elem = sorted_left.unshift()
        sorted_sequence.push(elem)

    while middle.count() > 0:
        elem = middle.unshift()
        sorted_sequence.push(elem)

    while sorted_right.count() > 0:
        elem = sorted_right.unshift()
        sorted_sequence.push(elem)

    return sorted_sequence


import random


def generate_sequence(n):
    start_sequence = DoubleLinkedList()
    for i in range(0, n):
        start_sequence.push(random.randint(0, 10000))
    return start_sequence


def check_sorted(dllist):
    elem = dllist.first()
    for i in range(1, dllist.count()):
        next_elem = dllist.get(i)
        if elem > next_elem:
            return False
        elem = next_elem
    return True


def main_dllist():
    n = 50
    start_sequence = generate_sequence(n)
    quick_sorted_sequence = quick_sort_dllist(start_sequence)
    assert check_sorted(quick_sorted_sequence)
    quick_sort_dllist(generate_sequence(0))
    quick_sort_dllist(generate_sequence(1))


main_dllist()
