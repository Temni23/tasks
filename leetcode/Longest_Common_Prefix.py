"""
Write a function to find the longest common prefix string.

Amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List

test_array = ["flower", "flow", "flight"]


def longest_common_prefix(strs: List[str]) -> str:
    pre = strs[0]

    for i in strs:
        while not i.startswith(pre):
            pre = pre[:-1]

    return pre


print(longest_common_prefix(test_array))