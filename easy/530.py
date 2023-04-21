from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.prev = None
        
        def dfs(root: TreeNode):
            if not root:
                return
            
            dfs(root.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, root.val - self.prev)
            self.prev = root.val
            dfs(root.right)
        
    
        dfs(root)
        return self.min_diff