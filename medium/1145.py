from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        c = [0, 0]
        def count_node(root: TreeNode):
            if not root:
                return 0
            
            left = count_node(root.left)
            right = count_node(root.right)
            if root.val == x:
                c[0], c[1] = left, right
            return left + right + 1

        return count_node(root) / 2 < max(max(c), n - sum(c) - 1)