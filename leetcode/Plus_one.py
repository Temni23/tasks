"""
You are given a large integer represented as an integer array digits.

 Each digit[i] is the ith digit of the integer. The digits are ordered

 from most significant to the least significant in left-to-right order.

 The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
from typing import List

test_arr = [1]


def plus_one(digits: List[int]) -> List[int]:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = -1
    digits[i] = digits[i] + 1
    while digits[i] not in numbers:
        digits[i] = 0
        try:
            digits[i - 1] = digits[i - 1] + 1
        except:
            digits.insert(0, 1)
            break
        i -= 1
    return digits


print(plus_one(test_arr))
