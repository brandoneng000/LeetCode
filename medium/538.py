from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        def dfs(root: TreeNode):
            if not root:
                return
            
            dfs(root.right)
            self.sum += root.val
            root.val = self.sum
            dfs(root.left)
        
        dfs(root)
        return root
