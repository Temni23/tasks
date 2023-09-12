"""
You are given a large integer represented as an integer array digits.

 Each digit[i] is the ith digit of the integer. The digits are ordered

 from most significant to the least significant in left-to-right order.

 The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
from typing import List

test_arr = [9,9]


def plus_one(digits: List[int]) -> List[int]:
    integer_digit = int(''.join(map(str, digits))) +1
    digits = list(map(int, str(integer_digit)))
    return digits


print(plus_one(test_arr))
