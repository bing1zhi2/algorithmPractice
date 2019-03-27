"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        re = self.list_all(root)
        return re != -1

    def list_all(self, curr: TreeNode):

        if curr is None:
            return 0
        # print("curr val", curr.val)

        left_height = self.list_all(curr.left)
        if left_height == -1:
            return -1

        right_height = self.list_all(curr.right)
        if right_height == -1:
            return -1

        if abs(right_height - left_height) > 1:
            return -1

        return max(left_height, right_height) + 1


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

s.isBalanced(t_root)
