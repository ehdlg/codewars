"""
Write a function named first_non_repeating_letter† that takes a string input,
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter.
For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons,
but your function should handle any Unicode character.
"""


def first_non_repeating_letter(s):
    if not s:
        return ""

    repeated_letters = []

    for i in range(len(s)):
        letter = s[i]

        if letter in repeated_letters:
            continue
        else:
            repeated_letters.append(letter.upper())
            repeated_letters.append(letter.lower())

        count = 0

        for other_letter in s[i:]:
            if letter.lower() == other_letter.lower():
                count += 1

            if count > 1:
                break

        if count == 1:
            return letter

    return ""
