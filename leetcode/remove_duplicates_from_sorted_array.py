"""
Given an integer array nums sorted in non-decreasing order.
 remove the duplicates in-place such that each unique element appears only once
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.
"""
from typing import List

test_list = [1, 1, 2]


def remove_duplicates(nums: List[int]) -> int:
    nums[:] = sorted(set(nums))
    return len(nums)


print(test_list)
print(remove_duplicates(test_list))
print(test_list)
