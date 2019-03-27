# -*- coding:utf-8 -*-
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
 How would you optimize the kthSmallest routine?

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:



    def kthSmallest(self, root: TreeNode, k: int) -> int:

        self.k = k
        self.res = None

        self.helper(root)
        return self.res

    def helper(self, n: TreeNode):
        # 向左找到一个最小的
        if n is None:
            return
        if n.left is not None:
            self.helper(n.left)
        self.k -= 1

        if self.k == 0:
            self.res = n.val
        # 如果右边有子结点 也要遍历
        self.helper(n.right)

    def findmin(self, node: TreeNode):
        if node is None:
            return None
        elif node.left is None:
            return node
        return self.findmin(node.left)

    def finmax(self, node: TreeNode):
        if node is not None:
            while node.right is not None:
                node = node.right
        return node


root = TreeNode(5)
n1 = TreeNode(3)
n2 = TreeNode(6)
n3 = TreeNode(2)
n4 = TreeNode(4)
n5 = TreeNode(1)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n3.left = n5

s = Solution()
# node = s.finmax(root)
# print(node.val)
# node = s.findmin(root)
# print(node.val)
m = s.kthSmallest(root, 4)
print(m)
