from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur_level_sum = root.val
        q = deque([root])

        while q:
            next_level = []
            next_level_sum = 0

            for node in q:
                node.val = cur_level_sum - node.val
                
                for child in node.left, node.right:
                    if child:
                        next_level.append(child)
                        next_level_sum += child.val
                
                if node.left and node.right:
                    total = node.left.val + node.right.val
                    node.left.val = node.right.val = total
            
            q = next_level
            cur_level_sum = next_level_sum
        
        return root