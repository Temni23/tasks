from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    sum_ = int(first_number, 2) + int(second_number, 2)
    if sum_ == 0:
        return "0"
    result = ""

    while sum_:
        result += str(sum_ % 2)
        sum_ //= 2
    return result[::-1]

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
