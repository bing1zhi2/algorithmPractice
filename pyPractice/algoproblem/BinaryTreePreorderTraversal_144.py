"""
Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7
"""
# Definition for a binary tree node.



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) :
        s = [root]
        result = []
        while s:
            tempNode = s.pop()
            if tempNode:
                result.append(tempNode.val)
                s.append(tempNode.right)
                s.append(tempNode.left)
        return result
