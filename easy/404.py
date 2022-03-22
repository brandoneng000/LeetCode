from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(leaf: Optional[TreeNode], left: bool) -> int:
            if left and not leaf.left and not leaf.right:
                return leaf.val
            
            res = 0
            if leaf.left:
                res += traverse(leaf.left, True)
            if leaf.right:
                res += traverse(leaf.right, False)

            return res

        return traverse(root, False)
