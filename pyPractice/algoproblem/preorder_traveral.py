# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        b = []
        self.visitNode(root, b)


        return b

    def visitNode(self,root, b):
        if root is not None:
            if root.val is not None:
                 b.append(root.val)
            self.visitNode(root.left, b)
            self.visitNode(root.right, b)