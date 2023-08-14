from typing import List, Tuple


def transpose_matrix(matrix: List[str], n: int, m: int) -> None:
    count = 0
    circle = 0
    len_matrix = len(matrix)
    for i in range(n * m):
        print(matrix[count + circle], sep=" ", end=" ")
        count += m
        if count >= len_matrix:
            circle += 1
            count = 0
            print("")


def read_input() -> Tuple[List[str], int, int]:
    n = int(input())
    m = int(input())
    matrix = [i for _ in range(n) for i in input().strip().split()]
    return matrix, n, m


def main():
    matrix, n, m = read_input()
    transpose_matrix(matrix, n, m)


if __name__ == '__main__':
    main()
