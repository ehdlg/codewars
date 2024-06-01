"""
 In this little assignment you are given a string of space separated numbers,
 and have to return the highest and lowest number.
"""

def solution(numbers):
    number_list = [int(x) for x in numbers.split()]
    min = max = number_list[0]
    
    for number in number_list[1:]:
        if number > max:
            max = number
        
        if number < min: 
            min = number

    return f'{max} {min}'


print(solution('12 23 43 -2 234'))