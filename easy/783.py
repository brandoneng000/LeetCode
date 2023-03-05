from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        cur_node = root
        stack = []
        result = []

        while True:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            elif stack:
                cur_node = stack.pop()
                result.append(cur_node.val)
                cur_node = cur_node.right
            else:
                break
        
        return min(result[index + 1] - result[index] for index in range(len(result) - 1))
