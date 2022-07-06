from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def min_branch(root: TreeNode, depth: int):
            if not root.left and not root.right:
                return depth
            
            left = right = float('inf')
            if root.left:
                left = min_branch(root.left, depth + 1)
            if root.right:
                right = min_branch(root.right, depth + 1)

            return min(left, right)
        
        return min_branch(root, 1)