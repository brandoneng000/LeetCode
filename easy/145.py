# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def traverse(root: Optional[TreeNode]):
        #     if root:
        #         traverse(root.left)
        #         traverse(root.right)
        #         result.append(root.val)

        # result = []
        # traverse(root)
        # return result

        stack = [root]
        result = []

        while stack:
            root = stack.pop()
            if root:
                result.append(root.val)
                stack.append(root.left)
                stack.append(root.right)

        return result[::-1]

