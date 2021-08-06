# -*- coding:utf-8 -*-

'''
二叉搜索树， 插入、删除
'''

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def work_tree(tree):
    # idx = 0
    if tree:
        print("tree node access:{}" .format(tree.data))
        work_tree(tree=tree.left)
        work_tree(tree=tree.right)

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

def find_min(tree):
    if tree is not None:
        if tree.left is not None:
            tree = tree.left
    return tree

def delete(tree, x):
    if tree is None:
        print("删除结点不存在")
    else:
        if x < tree.data:
            tree.left = delete(tree.left, x)
        elif x > tree.data:
            tree.right = delete(tree.right, x)
        else:
            # 如果左右儿子都不空,从右子树中找最小的,替换，
            if tree.right and tree.left:
                tmp = find_min(tree)
                tree.data = tmp.data
                tree.right = delete(tree.right, tmp.data)
            elif tree.right:
                tree = tree.right
            elif tree.left:
                tree = tree.left
            else:
                tree = None

            
    
    return tree

a = [1, 2, 3, 4, 5]
b = None
for i in a:
    b = insert(b, i)

work_tree(b)
aaa = find_min(b)
print(aaa.data)

delete(b,3)
print("------------after delete:")
delete(b,3)


work_tree(b)
