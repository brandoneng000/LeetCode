from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        temp = root
        node  = temp
        right_branches = collections.deque()
        while node:
            if node.right:
                right_branches.append(node.right)
                node.right = None
            if node.left:
                node.right = node.left
                node.left = None
            if not node.right and right_branches:
                node.right = right_branches.pop()
            node = node.right

        return root