from typing import List

def factorize(number: int) -> List[int]:
    result = []
    delitel = 2
    while delitel*delitel <= number:
        while number % delitel == 0:
            result.append(delitel)
            number = number / delitel
        delitel = delitel + 1
    if number > 1:
        result.append(int(number))
    return result

result = factorize(int(input()))
print(" ".join(map(str, result)))
