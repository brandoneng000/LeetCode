from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        vals = []

        def dfs(root: TreeNode):
            if not root:
                return
            
            dfs(root.left)
            vals.append(root.val)
            dfs(root.right)
        
        dfs(root)
        new_root = temp = TreeNode(vals.pop(0))
        while vals:
            node = TreeNode(vals.pop(0))
            temp.right = node
            temp = temp.right
        
        return new_root