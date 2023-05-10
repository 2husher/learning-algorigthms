def bubble_sort(numbers):
    for k in range(len(numbers) - 1, 0, -1):
        is_sorted = True
        for i in range(0, k, 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                is_sorted = False
        if is_sorted: break
    return numbers