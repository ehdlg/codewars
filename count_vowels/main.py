"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

VOWELS = set("aeiouAEIOU")


def get_count(string: str):
    count = 0

    for letter in string:
        if letter in VOWELS:
            count += 1

    return count


print(get_count("aeiou etsta"))
