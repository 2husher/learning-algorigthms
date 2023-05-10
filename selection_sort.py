def selection_sort(numbers):
    for k in range(0, len(numbers) - 1):
        for i in range(k + 1, len(numbers)):
            if numbers[k] > numbers[i]:
                numbers[k], numbers[i] = numbers[i], numbers[k]
    return numbers