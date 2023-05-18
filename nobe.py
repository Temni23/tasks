# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


    def solution(node):
        while node:
            print(node.value)
            node = node.next_item


def read_input():
    nobe = []
    list_len = int(input())
    for i in range(1, list_len):
        nobe.append(Node(input(),nobe[i-1]))


if __name__ == '__main__':
    task_list = read_input()
    solution(task_list)
