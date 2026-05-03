from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root: TreeNode):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left == right >= 0:
                res.append(left + 1)
                return left + 1
            
            return -1
        
        res = []
        
        dfs(root)
        return (1 << sorted(res)[-k]) -1 if k <= len(res) else -1