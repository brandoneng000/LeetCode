from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(root: TreeNode, start: int):
            depth = 0

            if not root:
                return depth
            
            left = dfs(root.left, start)
            right = dfs(root.right, start)

            if root.val == start:
                self.res = max(left, right)
                depth = -1
            elif left >= 0 and right >= 0:
                depth = max(left, right) + 1
            else:
                dist = abs(left) + abs(right)
                self.res = max(self.res, dist)
                depth = min(left, right) - 1
            
            return depth
        
        self.res = 0
        dfs(root, start)
        return self.res