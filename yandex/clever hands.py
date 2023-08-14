# ID 86853734
from typing import List


def get_points(keyboard: List[str], keys: int) -> int:
    points = 0
    unic_keys_count = {}
    for key in keyboard:
        if key in unic_keys_count:
            unic_keys_count[key] += 1
        else:
            unic_keys_count[key] = 1
    for elements in unic_keys_count:
        if 0 < unic_keys_count[elements] <= keys:
            points += 1

    return points


if __name__ == '__main__':
    keys_for_task = int(input()) * 2
    matrix = [i for _ in range(4) for i in input().strip() if i != "."]
    print(get_points(matrix, keys_for_task))
