from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.res = None
        self.max_depth = 0

        def dfs(root: TreeNode, depth: int):
            if not root:
                return depth - 1
            
            self.max_depth = max(self.max_depth, depth)
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)

            if left == right == self.max_depth:
                self.res = root
            
            return max(left, right)
        
        dfs(root, 0)
        return self.res