"""
Given two strings s1 and s2, we want to visualize how different the two strings are.
 We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1;
the maximum for 'b' is 3 from s2.
In the following we will not consider letters when the maximum of their occurrences
 is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string:
"1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum
for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2
appears as many times as its maximum if this maximum is strictly greater than 1;
these letters will be prefixed by the number of the string where they appear with
 their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh;
it contains the prefix) will be in decreasing order of their length and when
they have the same length sorted in ascending lexicographic order (letters and digits -
more precisely sorted by codepoint); the different groups will be separated by '/'.
 See examples and "Example Tests".
"""


def mix(s1, s2):
    letters = []
    count = []
    sum_string = s1 + s2

    for letter in sum_string:
        if letter.islower() and letter not in letters:
            letters.append(letter)

    for letter in letters:
        count_s1 = s1.count(letter)
        count_s2 = s2.count(letter)

        if count_s1 <= 1 and count_s2 <= 1:
            continue

        if count_s1 > count_s2:
            count.append(f"1:{letter * count_s1}")
        elif count_s2 > count_s1:
            count.append(f"2:{letter * count_s2}")
        else:
            count.append(f"=:{letter * count_s1}")

    count.sort(key=lambda x: (-len(x), x))

    return "/".join(count)


print(mix("Are they here", "yes, they are here"))
