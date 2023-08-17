# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be
# if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

nums, target = [1,2,3,4,5,10], 5


def search_insert(array: list, insert_num: int) -> int:
    middle = len(array) // 2
    first = 0
    last = len(array) - 1
    if array[first] >= insert_num:
        return 0
    if array[last] == insert_num:
        return last
    if array[last] < insert_num:
        return last + 1
    if array[middle] == insert_num:
        return middle

    if insert_num > array[middle]:
        while target > array[middle]:
            middle += 1
        return middle
    else:
        while insert_num <= array[middle]:
            middle -= 1
        return middle + 1


print(search_insert(nums, target))
