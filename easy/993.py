from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth = 0
        stack = [(-1, root)]
        result = []
        children = []
        while stack and len(result) != 2:
            val = stack.pop()
            parent = val[0]
            node = val[1]
            if node.left:
                children.append((node.val, node.left))
            if node.right:
                children.append((node.val, node.right))
            if node.val == x or node.val == y:
                result.append((parent, depth))

            if not stack:
                stack = children
                children = []
                depth += 1

        return result[0][1] == result[1][1] and result[0][0] != result[1][0]