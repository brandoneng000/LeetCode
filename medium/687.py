from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root: TreeNode):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)

            left_node = right_node = 0
            if root.left and root.left.val == root.val:
                left_node = left + 1
            if root.right and root.right.val == root.val:
                right_node = right + 1
            self.res = max(self.res, left_node + right_node)
            return max(left_node, right_node)

        dfs(root)
        return self.res