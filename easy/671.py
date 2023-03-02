from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        stack = []
        result = []
        cur_node = root

        while stack or cur_node:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            elif stack:
                cur_node = stack.pop()
                if cur_node.val not in result:
                    result.append(cur_node.val)
                cur_node = cur_node.right
            
        result.sort()

        return result[1] if len(result) >= 2 else -1
