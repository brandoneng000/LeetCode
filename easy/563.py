from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        tilt = []
        def dfs(root: TreeNode):
            if not root.left and not root.right:
                tilt.append(0)
                return root.val
            
            left, right = 0, 0
            if root.left:
                left = dfs(root.left)
            
            if root.right:
                right = dfs(root.right)
            
            tilt.append(abs(right - left))
            return root.val + left + right
        
        dfs(root)
        return sum(tilt)
        
        
        