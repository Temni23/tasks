# ID 86822422
from typing import List, Tuple


def get_points(keyboard: List[int], k: int) -> int:
    points = 0
    count = [0] * len(keyboard)
    for key in keyboard:
        count[key] += 1
    for num in count:
        if 0 < num <= k * 2:
            points += 1
    return points


def read_input() -> Tuple[List[int], int]:
    k = int(input())
    matrix = [int(i) for _ in range(4) for i in input().strip() if i != "."]
    return matrix, k


def main():
    keyboard, k = read_input()
    print(get_points(keyboard, k))


if __name__ == '__main__':
    main()
