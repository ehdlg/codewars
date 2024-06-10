"""
Write a method that takes an array of consecutive (increasing) letters as input
and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be
missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.
"""


def find_missing_letter(chars):
    for i, letter in enumerate(chars):
        pos = ord(letter)
        next_pos = ord(chars[i + 1])
        if next_pos - pos != 1:
            return chr(pos + 1)
