from typing import List


def merge_sorted_list(list_1: List, list_2: List) -> List:
    length_1 = len(list_1)
    length_2 = len(list_2)
    result = []

    i = j = 0

    while length_1 > i and length_2 > j:
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    result += list_1[i:] + list_2[j:]

    return result


def split_and_merge(unsorted_list: List) -> List:
    middle = len(unsorted_list) // 2
    part_1 = unsorted_list[:middle]
    part_2 = unsorted_list[middle:]

    if len(part_1) > 1:
        part_1 = split_and_merge(part_1)
    if len(part_2) > 1:
        part_2 = split_and_merge(part_2)

    return merge_sorted_list(part_1, part_2)



if __name__ == "__main__":
    x = list(range(1, 10, 2))
    y = list(range(2, 11, 2))

    print(split_and_merge([55, 77, 8, -5, 16, 25, 32, 8, 777, 414]))
