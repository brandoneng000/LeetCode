from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def merge(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            if not root1:
                return root2
            if not root2:
                return root1
            
            new_root = TreeNode(root1.val + root2.val)

            if root1.left or root2.left:
                new_root.left = merge(root1.left, root2.left)
            if root1.right or root2.right:
                new_root.right = merge(root1.right, root2.right)
        
            return new_root
        
        return merge(root1, root2)