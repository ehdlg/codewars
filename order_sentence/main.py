"""
Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.
"""


def order(sentence):
    sentence = sentence.split()
    sentence_list = [None for _ in range(len(sentence))]

    for word in sentence:
        for letter in word:
            if letter.isnumeric():
                sentence_list[int(letter) - 1] = word

    return " ".join(sentence_list)
