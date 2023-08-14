import re


def is_palindrome(line: str) -> bool:
    line = re.sub(r"[^a-zA-Zа-яА-ЯёЁ]+", "", line).lower()
    if line == line[::-1]:
        return True
    return False


print(is_palindrome(input().strip()))
