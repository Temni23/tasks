from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []
    check_cords = [
        (row + 1, col),
        (row - 1, col),
        (row, col - 1),
        (row, col + 1),
    ]
    for cords in check_cords:
        if cords[0] >= 0 and cords[1] >= 0:
            try:
                neighbour = matrix[cords[0]][cords[1]]
                result.append(neighbour)
            except IndexError:
                pass
    return sorted(result)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
