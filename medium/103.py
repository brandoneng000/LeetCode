from typing import List, Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        stack = collections.deque([root])
        res = []
        children = 1
        level = []
        alternate = False

        while stack:
            node = stack.popleft()
            children -= 1
            level.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
            if not children:
                if alternate:
                    level.reverse()
                res.append(level.copy())
                children = len(stack)
                level.clear()
                alternate = not alternate
        
        return res

