from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def sum_tree(root: TreeNode):
            if not root:
                return 0
            left = sum_tree(root.left)
            right = sum_tree(root.right)
            self.res = max(self.res, left * (total_tree - left), right * (total_tree - right))

            return root.val + left + right
        
        mod = 1000000007
        total_tree = 0
        self.res = 0
        total_tree = sum_tree(root)
        sum_tree(root)

        return self.res % mod
