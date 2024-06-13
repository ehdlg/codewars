"""
Complete the function that

    accepts two integer arrays of equal length
    compares the value each member in one array to the corresponding member in the other
    squares the absolute value difference between those two values
    and returns the average of those squared absolute value difference between each member pair.

"""


def solution(a: list[int], b: list[int]):
    total = sum([abs(x - y) ** 2 for x, y in zip(a, b)]) / len(a)

    return total


print(solution([1, 2, 3], [4, 5, 6]))
