def quick_sort(sequence):
    if len(sequence) < 2: return sequence

    left, middle, right = divide(sequence)      # n

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    sorted_sequence = sorted_left + middle + sorted_right
    return sorted_sequence


def divide(sequence):
    middle_index = len(sequence) // 2
    middle_elem = sequence[middle_index]

    left = []
    middle = []
    right = []
    for elem in sequence:       # n
        if elem < middle_elem:
            left.append(elem)
        elif elem > middle_elem:
            right.append(elem)
        else:
            middle.append(elem)
    return left, middle, right


import random


def main():
    n = 30
    start_sequence = []
    for i in range(0, n):
        start_sequence.append(random.randint(0, 10000))

    checked = sorted(start_sequence.copy())

    quick_sorted = quick_sort(start_sequence.copy())

    # print(f"QUICK SORTED: {quick_sorted}")

    assert quick_sorted == checked


main()
