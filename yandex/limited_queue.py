class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_size = n
        self.head = 0
        self.tail = 0
        self.actual_size = 0

    def size(self):
        return self.actual_size

    def push(self, value):
        if self.actual_size != self.max_size:
            self.queue[self.tail] = value
            self.actual_size += 1
            self.tail = (self.tail + 1) % self.max_size
        else:
            print("error")

    def pop(self):
        if self.size() == 0:
            return None
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.actual_size -= 1
        self.head = (self.head + 1) % self.max_size
        return value

    def peek(self):
        return self.queue[self.head]


command_all = int(input())
queue = MyQueueSized(int(input()))

def check_command(command: str) -> None:
    if command == "size":
        print(queue.size())
    if command == "pop":
        print(queue.pop())
    if command.startswith("pu"):
        queue.push(int(command.split()[1]))
    if command == "peek":
        print(queue.peek())

if __name__ == "__main__":
    for _ in range(command_all):
        check_command(input())
