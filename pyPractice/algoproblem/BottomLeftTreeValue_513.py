"""
Bottom Left Tree Value

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.

"""
from collections import deque  # 双端队列


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        deq = deque()
        deq.append(root)

        lastdep = None

        while len(deq) > 0:
            lastdep = deq.copy()
            deq2 = self.enqueue(deq)
            deq = deq2
        # print(lastdep.popleft().val)
        leftnode = lastdep.popleft()

        return leftnode.val

    def enqueue(self, deq1: deque):
        deq2 = deque()
        while len(deq1) > 0:
            tempNode = deq1.popleft()
            print(tempNode.val)
            if tempNode.left:
                deq2.append(tempNode.left)
            if tempNode.right:
                deq2.append(tempNode.right)
        return deq2


s = Solution()

t_root = TreeNode(1)
t_1 = TreeNode(2)
t_2 = TreeNode(2)
t_3 = TreeNode(3)
t_4 = TreeNode(3)
t_5 = TreeNode(4)
t_6 = TreeNode(4)

t_root.left = t_1
t_root.right = t_2
t_1.left = t_3
t_1.right = t_4
t_3.left = t_5
t_3.right = t_6

s.findBottomLeftValue(t_root)
