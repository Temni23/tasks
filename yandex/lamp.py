# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(node) -> int:
    if node is None:
        return
    v = [node]
    max_v = 0
    while v:
        vn = []
        for x in v:
            if x.value > max_v:
                max_v = x.value
            if x.left:
                vn += [x.left]
            if x.right:
                vn += [x.right]
        v = vn
    return max_v
