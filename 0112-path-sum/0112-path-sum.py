# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: #Solution 
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # If leaf node
        if not root.left and not root.right:
            return targetSum == root.val

        # Recurse on children nodes 
        remaining = targetSum - root.val

        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))
