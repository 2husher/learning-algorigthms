from bubble_sort import bubble_sort
from insert_sort import insert_sort
from selection_sort import  selection_sort
from random import randint


max_numbers = 30


def random_list(count):
    numbers = []
    for i in range(count, 0, -1):
        numbers.append(randint(0, 10000))
    return numbers


def is_sorted(numbers):
    for i in range(0, len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True


def test_bubble_sort():
    numbers = random_list(max_numbers)
    bubble_sorted = bubble_sort(numbers)
    assert is_sorted(bubble_sorted)


def test_insert_sort():
    numbers = random_list(max_numbers)
    insert_sorted = insert_sort(numbers)
    assert is_sorted(insert_sorted)


def test_selection_sort():
    numbers = random_list(max_numbers)
    selection_sorted = selection_sort(numbers)
    assert is_sorted(selection_sorted)


test_bubble_sort()
test_insert_sort()
test_selection_sort()
