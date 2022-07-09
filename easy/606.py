from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        def dfs(root: TreeNode):
            if not root.left and not root.right:
                return str(root.val)

            res = f"{root.val}"
            if root.left:
                res += f"({dfs(root.left)})"
            else:
                res += "()"
            if root.right:
                res += f"({dfs(root.right)})"

            return res
            
        return dfs(root)