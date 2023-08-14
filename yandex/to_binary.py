def to_binary(number: int) -> str:
    if number == 0:
        return "0"
    result = ""

    while number:
        result += str(number % 2)
        number //= 2
    return result[::-1]


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
