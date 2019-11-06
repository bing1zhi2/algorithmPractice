# -*- coding:utf-8 -*-


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


def insert(tree, x):
    if tree is None:
        tree = Node()
        tree.data = x
    else:
        if x < tree.data:
            tree.left = insert(tree.left, x)
        elif x > tree.data:
            tree.right = insert(tree.right, x)
    return tree


a = [1, 2, 3, 4, 5]
b = None
for i in a:
    b = insert(b, i)

print(b)
