# ID 86891743
from typing import List


def find_distance(street_plan: List[int]) -> List[int]:
    result = [0 for _ in range(len(street_plan))]
    counter = 0
    empty_area_index = [i for i in range(len(street_plan)) if street_plan[i] == 0]
    first_empty = empty_area_index[0]
    last_empty = empty_area_index[-1]
    # заполняем данные от первого ноля до левой границы
    for _ in range(first_empty):
        counter += 1
        result[first_empty - counter] = counter

    counter = 0

    # заполняем данные от первого ноля до правой границы
    for _ in range(len(street_plan) - 1 - last_empty):
        counter += 1
        result[last_empty + counter] = counter

    for number in range(len(empty_area_index) - 1):
        counter = 0
        left_border = empty_area_index[number]
        right_border = empty_area_index[number + 1]
        for _ in range((right_border - left_border) // 2):
            counter += 1
            result[left_border + counter] = counter
            result[right_border - counter] = counter

    return result


if __name__ == "__main__":
    street_length = int(input())
    street_map = [int(number) for number in input().strip().split()]
    distance = find_distance(street_map)
    if distance is None:
        print("На этой улице нет участков.")
    else:
        print(*distance, sep=" ")
