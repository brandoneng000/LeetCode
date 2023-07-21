from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if not root.left and not root.right:
            if root.val < limit:
                return None
            else:
                return root
        else:
            root.left = self.sufficientSubset(root.left, limit - root.val)
            root.right = self.sufficientSubset(root.right, limit - root.val)
            if not root.left and not root.right:
                return None
            else:
                return root

    # def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
    #     def dfs(root: TreeNode, total: int):
    #         if not root:
    #             return None
            
    #         left = dfs(root.left, total + root.val)
    #         right = dfs(root.right, total + root.val)

    #         if not left and not right:
    #             if total + root.val < limit:
    #                 return None
    #             if root.left or root.right:
    #                 return None

    #         root.left = left
    #         root.right = right

    #         return root
        
    #     return dfs(root, 0)