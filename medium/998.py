from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     res = root
    #     parent = None
    #     while root and root.val > val:
    #         parent = root
    #         root = root.right
        
    #     if not parent:
    #         return TreeNode(val, root)
    #     else:
    #         parent.right = TreeNode(val, root)

    #     return res
    
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val < val:
            return TreeNode(val, root)
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
