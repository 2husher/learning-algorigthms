def insert_sort(numbers):
    for k in range(1, len(numbers)):
        for i in range(k, 0, -1):
            if numbers[i] < numbers[i - 1]:
                numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            else:
                break
    return numbers