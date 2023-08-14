# ID 87478400

from operator import add, floordiv, mul, sub
from typing import List

OPERATORS = {
    '+': add,
    '-': sub,
    '/': floordiv,
    '*': mul
}


class StackEmptyException(Exception):
    pass


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item: int):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise StackEmptyException('Stack is empty')


def calculator(stack, elem_list: List[str]):
    for elem in elem_list:
        if elem not in OPERATORS:
            stack.push(int(elem))
        else:
            try:
                num_a, num_b = stack.pop(), stack.pop()
                stack.push(OPERATORS[elem](num_b, num_a))
            except StackEmptyException:
                print('Stack is empty')
    return stack.pop()


if __name__ == '__main__':
    stack = Stack()
    elem_list = input().split()
    print(calculator(stack, elem_list))
