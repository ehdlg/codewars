""" 
* If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
* The sum of these multiples is 23.
* Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
* Additionally, if the number is negative, return 0.
* Note: If the number is a multiple of both 3 and 5, only count it once.
"""
def solution(number: int):
    if number <= 0:
        return 0

    isMultiple = lambda x: x % 3 == 0 or x % 5 == 0  # noqa: E731
    total = 0

    for n in range(3, number):
        if isMultiple(n):
            total += n

    return total


