from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(root: TreeNode):
            if not root:
                return []
            
            letter = chr(root.val + ord('a'))
            
            if not root.left and not root.right:
                return [letter]
            
            left = dfs(root.left)
            right = dfs(root.right)

            return [letters + letter for letters in left + right]
        
        return min(dfs(root))