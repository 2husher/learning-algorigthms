def quick_sort(sequence):
    if len(sequence) < 2: return sequence

    middle_index = len(sequence) // 2
    middle_elem = sequence[middle_index]

    left = []
    middle = []
    right = []
    for elem in sequence:
        if elem < middle_elem:
            left.append(elem)
        elif elem > middle_elem:
            right.append(elem)
        else:
            middle.append(elem)

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    sorted_sequence = sorted_left + middle + sorted_right
    return sorted_sequence


import random


def main():
    n = 50
    start_sequence = []
    for i in range(0, n):
        start_sequence.append(random.randint(0, 10000))

    assert quick_sort(start_sequence) == sorted(start_sequence)

main()
