from typing import List

list1 = [1, 2, 4]
list2 = [1, 3, 4]


def merge_two_sorted_list(list1: List[int], list2: List[int]) -> List[int]:
    index_1 = index_2 = 0
    result = []
    length_1 = len(list1)
    length_2 = len(list2)

    while length_1 > index_1 and length_2 > index_2:
        if list1[index_1] > list2[index_2]:
            result.append(list2[index_2])
            index_2 += 1
        else:
            result.append(list1[index_1])
            index_1 += 1
    result += list1[index_1:] + list2[index_2:]
    return result


print(merge_two_sorted_list(list1, list2))
