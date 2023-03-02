from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # stack = [root]
        # nums = []
        # nums_set = set()

        # while stack:
        #     node = stack.pop(0)
        #     if node:
        #         nums.append(node.val)
        #         stack.append(node.left)
        #         stack.append(node.right)

        # for num in nums:
        #     if num in nums_set:
        #         return True
        #     else:
        #         nums_set.add(k - num)
        
        # return False
        stack = [root]
        nums = set()

        while stack:
            node = stack.pop(0)
            if node:
                if node.val in nums:
                    return True
                else:
                    nums.add(k - node.val)
                    stack.append(node.left)
                    stack.append(node.right)
        
        return False