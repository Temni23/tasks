"""
Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


def str_in_str(haystack: str, needle: str) -> int:
    needle_length = len(needle)
    for index in range(len(haystack)):
        if haystack[index:index + needle_length] == needle:
            return index
    return -1


haystack_test, needle_test = 'leetcode', 'leeto'

print(str_in_str(haystack_test, needle_test))
