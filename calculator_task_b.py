# Решение 87349964

from operator import add, floordiv, mul, sub
from typing import List

OPERATORS = {
    '+': add,
    '-': sub,
    '/': floordiv,
    '*': mul
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: int):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('Stack is empty')


def calculator(stack, elem_list: List[str]):
    for elem in elem_list:
        if elem not in OPERATORS:
            stack.push(int(elem))
        else:
            num_a, num_b = stack.pop(), stack.pop()
            stack.push(OPERATORS[elem](num_b, num_a))
    return stack.pop()


if __name__ == '__main__':
    stack = Stack()
    elem_list = list(input().split())
    print(calculator(stack, elem_list))
