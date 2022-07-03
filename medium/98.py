from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check_tree(root: TreeNode, lower: int, upper: int):
            if not root:
                return True
            
            if lower < root.val < upper:
                return check_tree(root.left, lower, root.val) and check_tree(root.right, root.val, upper)
            else:
                False
            
        return check_tree(root, lower = -float('inf'), upper = float('inf'))