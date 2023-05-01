def is_power_of_four(number: int) -> bool:
    if number <= 0:
        return False
    while number != 1:
        if number % 4 == 0:
            number //= 4
        else:
            return False
    return True

print(is_power_of_four(int(input())))
