"""
Given an array (arr) as an argument complete the function countSmileys that should
return the total number of smiling faces.

Rules for a smiling face:

    Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    Every smiling face must have a smiling mouth that should be marked with either ) or D

No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]
"""

import re


def count_smileys(arr):
    regex = r"^[;:][-~]?[)D]$"

    count = sum(1 for x in arr if re.match(regex, x))

    return count
