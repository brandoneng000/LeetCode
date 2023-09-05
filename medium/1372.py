from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode, zigzag: int, right: bool):
            if not root:
                return zigzag - 1
            
            if right:
                return max(zigzag, dfs(root.left, zigzag + 1, False), dfs(root.right, 1, True))
            else:
                return max(zigzag, dfs(root.left, 1, False), dfs(root.right, zigzag + 1, True))
        
        return max(dfs(root.left, 1, False), dfs(root.right, 1, True))