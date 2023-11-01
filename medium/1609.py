from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        level = True

        while q:
            size = len(q)
            if level:
                prev = -float('inf')
            else:
                prev = float('inf')

            for _ in range(size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if level:
                    if prev < node.val and node.val % 2 == 1:
                        prev = node.val
                    else:
                        return False
                else:
                    if prev > node.val and node.val % 2 == 0:
                        prev = node.val
                    else:
                        return False
            
            level = not level
        
        return True