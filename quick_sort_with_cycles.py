def quick_sort_with_cycles(sequence):
    sequence = [sequence]
    is_sorted = False

    while not is_sorted:        # log n
        is_sorted = True

        sequence2 = []
        while len(sequence) > 0:
            arr = sequence.pop(0)

            if len(arr) > 1:
                is_sorted = False

                left, middle, right = divide(arr)   # n

                sequence2.append(left)
                for x in middle:
                    sequence2.append([x])
                sequence2.append(right)

            elif len(arr) == 1:
                sequence2.append(arr)
            else:
                pass    # do nothing, skip []
        sequence = sequence2
    sequence2 = []
    for arr in sequence:
        sequence2.append(arr[0])
    return sequence2


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
    n = 50
    start_sequence = []
    for i in range(0, n):
        start_sequence.append(random.randint(0, 100))


    checked = sorted(start_sequence.copy())

    quick_sorted_with_cycles = quick_sort_with_cycles(start_sequence.copy())

    # print(f"QUICK SORTED: {quick_sorted_with_cycles}")

    assert quick_sorted_with_cycles == checked

main()
