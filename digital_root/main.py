"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.
"""


def digital_root(n: int):
    if n / 10 < 1:
        return n

    n = sum([int(number) for number in str(n)])

    return digital_root(n)
