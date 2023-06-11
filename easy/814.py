from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: TreeNode):
            if not root:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)
            if not left:
                root.left = None
            
            if not right:
                root.right = None
            
            return (root.val == 1) or left or right
        
        return root if dfs(root) else None