class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class QueueNode:
    def __init__(self):
        self.head = None
        self.tail = None
        self.actual_size = 0

    def get(self):
        if self.head == None:
            return "error"
        data = self.head.value
        self.head = self.head.next_item
        self.actual_size -= 1
        if self.head is None:
            self.tail = None
        return data

    def put(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_item = node
            self.tail = node
        self.actual_size += 1

    def size(self):
        return self.actual_size


command_all = int(input())
queue = QueueNode()


def check_command(command: str) -> None:
    if command == "size":
        print(queue.size())
    if command == "get":
        print(queue.get())
    if command.startswith("pu"):
        queue.put(int(command.split()[1]))


if __name__ == "__main__":
    for _ in range(command_all):
        check_command(input())
