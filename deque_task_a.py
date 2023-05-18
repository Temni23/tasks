# ID 87349525

class Deque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [None] * max_size
        self.start = 0
        self.end = 0
        self.size = 0

    def push_back(self, value):
        if self.size == self.max_size:
            print("error")
            return
        self.data[self.end] = value
        self.end = (self.end + 1) % self.max_size
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            print("error")
            return
        self.start = (self.start - 1) % self.max_size
        self.data[self.start] = value
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return "error"

        value = self.data[self.start]
        self.data[self.start] = None
        self.start = (self.start + 1) % self.max_size
        self.size -= 1
        return value

    def pop_back(self):
        if self.size == 0:
            return "error"
        self.end = (self.end - 1) % self.max_size
        value = self.data[self.end]
        self.data[self.end] = None
        self.size -= 1
        return value


def check_command(command, deque):
    if command.startswith("push_back"):
        deque.push_back(int(command.split()[1]))
    if command.startswith("push_front"):
        deque.push_front(int(command.split()[1]))
    if command == "pop_front":
        print(deque.pop_front())
    if command == "pop_back":
        print(deque.pop_back())


if __name__ == "__main__":
    commands_number = int(input())
    my_deque = Deque(int(input()))
    for _ in range(commands_number):
        check_command(input(), my_deque)
