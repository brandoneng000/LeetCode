from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.res = []
        self.index = 0

        def dfs(root: TreeNode):
            if self.res == [-1]:
                return
            if not root:
                return
            
            if root.val != voyage[self.index]:
                self.res = [-1]
                return
            
            self.index += 1
            if root.left and root.right:
                if root.left.val != voyage[self.index]:
                    self.res.append(root.val)
                    dfs(root.right)
                    dfs(root.left)
                    return
            dfs(root.left)
            dfs(root.right)
            
        
        dfs(root)
        return self.res