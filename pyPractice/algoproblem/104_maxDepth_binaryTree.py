# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        

        return self.visitNode(root)

    
    def visitNode(self, root:TreeNode) -> int:
        print("visit:",root.val)
        if root is None:
            return 0
        else:
            if root.left is None and root.right is None:
                return 1
            else:
                left_depth = self.visitNode(root.left) 
                right_depth = self.visitNode(root.right) 

                currNodedepth = max(left_depth, right_depth) + 1

                return currNodedepth




s = Solution()

root = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)

node20.left = node15
node20.right = node7

root.left = node9
root.right = node20

b = s.maxDepth(root)
print(b)

