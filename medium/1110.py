from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        self.res = []

        def dfs(root: TreeNode):
            if not root:
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in delete:
                if root.left:
                    self.res.append(root.left)
                if root.right:
                    self.res.append(root.right)
                return None

            return root

        node = dfs(root)
        if node:
            self.res.append(node)
        
        return self.res