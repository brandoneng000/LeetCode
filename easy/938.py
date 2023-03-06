from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # cur_node = root
        # stack = []
        # result = 0

        # while cur_node or stack:
        #     if cur_node:
        #         stack.append(cur_node)
        #         cur_node = cur_node.left
        #     elif stack:
        #         cur_node = stack.pop()
        #         if low <= cur_node.val <= high:
        #             result += cur_node.val
        #         cur_node = cur_node.right

        # return result

        stack = [root]
        result = 0
        while stack:
            cur_node = stack.pop()
            if cur_node:
                if low <= cur_node.val <= high:
                    result += cur_node.val
                if low < cur_node.val:
                    stack.append(cur_node.left)
                if cur_node.val < high:
                    stack.append(cur_node.right)
        
        return result