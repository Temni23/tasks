# ID 87485051

class DequeFullException(Exception):
    pass


class DequeEmptyException(Exception):
    pass


class Deque:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__data = [None] * max_size
        self.__start = 0
        self.__end = 0
        self.__size = 0

    def push_back(self, value):
        if self.__size == self.__max_size:
            raise DequeFullException("The queue is full")
        self.__data[self.__end] = value
        self.__end = (self.__end + 1) % self.__max_size
        self.__size += 1

    def push_front(self, value):
        if self.__size == self.__max_size:
            raise DequeFullException("The queue is full")
        self.__start = (self.__start - 1) % self.__max_size
        self.__data[self.__start] = value
        self.__size += 1

    def pop_front(self):
        if self.__size == 0:
            raise DequeEmptyException("The queue is empty")
        value = self.__data[self.__start]
        self.__data[self.__start] = None
        self.__start = (self.__start + 1) % self.__max_size
        self.__size -= 1
        return value

    def pop_back(self):
        if self.__size == 0:
            raise DequeEmptyException("The queue is empty")
        self.__end = (self.__end - 1) % self.__max_size
        value = self.__data[self.__end]
        self.__data[self.__end] = None
        self.__size -= 1
        return value


def check_command(command, deque):
    if len(command) > 1:
        return getattr(deque, command[0])(int(command[1]))
    return getattr(deque, command[0])()


if __name__ == "__main__":
    commands_number = int(input())
    my_deque = Deque(int(input()))
    for _ in range(commands_number):
        try:
            result = check_command(input().split(), my_deque)
            if isinstance(result, int):
                print(result)
        except DequeEmptyException:
            print("error")
        except DequeFullException:
            print("error")
