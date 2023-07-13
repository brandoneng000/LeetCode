from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root: TreeNode, small: int, large: int):
            if not root:
                return
            self.res = max(self.res, abs(small - root.val), abs(large - root.val))
            small = min(small, root.val)
            large = max(large, root.val)
            dfs(root.left, small, large)
            dfs(root.right, small, large)

        dfs(root, root.val, root.val)
        return self.res