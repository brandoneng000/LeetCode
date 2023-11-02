from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode):
            if not root:
                return (0, 0)
            
            left_val, left_count = dfs(root.left)
            right_val, right_count = dfs(root.right)

            subtree_sum = left_val + right_val + root.val
            subtree_count = left_count + right_count + 1

            if root.val == subtree_sum // subtree_count:
                self.res += 1
            
            return (subtree_sum, subtree_count)
            
        self.res = 0
        dfs(root)
        return self.res