from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root: TreeNode, height):
            if not root:
                return height
            
            return max(dfs(root.left, height + 1), dfs(root.right, height + 1))

        left = dfs(root.left, 1)
        right = dfs(root.right, 1)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)