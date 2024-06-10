"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""


def calculate_score(word):
    return sum([ord(letter) - ord("a") + 1 for letter in word])


def high(x):
    x = x.split(" ")
    winning_word = x[0]
    score = calculate_score(winning_word)

    for word in x[1:]:
        new_score = calculate_score(word)
        if new_score > score:
            winning_word = word
            score = new_score

    return winning_word


print(high("asjdk ka a kjasdflkjw aksjfdlkajflj io word alksjdflkwj"))
