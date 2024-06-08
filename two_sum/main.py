def two_sum(numbers, target):
    repeated_numbers = []

    for i, number in enumerate(numbers):
        if i in repeated_numbers:
            continue

        for j, another_number in enumerate(numbers[i + 1 :], start=i + 1):
            if number + another_number == target:
                return (i, j)

        repeated_numbers.append(i)
