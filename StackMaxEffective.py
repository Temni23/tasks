class StackMaxEffective:

    def __init__(self):
        self.items = []

    def push(self, item):
        if self.items:
            new_max = max(item, self.items[-1][1])
        else:
            new_max = item
        self.items.append((item, new_max))

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("error")


    def get_max(self):
        if self.items:
            return self.items[-1][1]
        return None


stack = StackMaxEffective()


def check_command(command: str) -> None:
    if command == "get_max":
        print(stack.get_max())
    if command == "pop":
        stack.pop()
    if command.startswith("pu"):
        stack.push(int(command.split()[1]))


if __name__ == "__main__":
    for _ in range(int(input())):
        check_command(input())
