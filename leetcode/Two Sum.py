# Given an array of integers nums and an integer target, return indices of
# the two numbers such that they add up to target.
# # You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
from typing import List

nums = [3, 2, 3]
target = 6


def two_sum(nums: List[int], target: int) -> List[int] or bool:
    cache = {}
    for index, num in enumerate(nums):
        different = target - num

        if different in cache:
            return [cache[different], index]
        cache[num] = index

    return False


result = two_sum(nums, target)
print(result)
