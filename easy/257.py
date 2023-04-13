from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.path = []
        self.res = []
        def dfs(root: TreeNode):
            if not root.left and not root.right:
                self.path.append(str(root.val))
                self.res.append("->".join(self.path))
                self.path.pop()
                return

            self.path.append(str(root.val))
            if root.left:
                dfs(root.left)

            if root.right:
                dfs(root.right)
            
            self.path.pop()
        
        dfs(root)
        return self.res