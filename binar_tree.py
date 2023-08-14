# betta

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = s

    def __del_one_child(self, child, parent):
        if parent.left == child:
            if child.left is None:
                parent.left = child.right
            elif child.right is None:
                parent.left = child.right
        elif parent.right == child:
            if child.left is None:
                parent.right = child.right
            elif child.right is None:
                parent.right = child.right

    def __find(self, node, parent, value):
        if value == node.data:
            return node, parent, True
        if node is None:
            return None, parent, False
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node, node.left)
        return node, parent

    def append(self, obj: Node):
        if self.root is None:  # Если в дереве нет корня, добавляем объект в корень
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_tree_wide(self, node):
        if node is None:
            return
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        if s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)


t = Tree()

v = [10, 5, 7, 16, 13, 2, 20]

for values in v:
    t.append(Node(values))

t.show_tree_wide(t.root)
t.del_node(23)


