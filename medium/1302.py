from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        
        while q:
            size = len(q)
            cur = 0

            for _ in range(size):
                node = q.popleft()
                cur += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return cur
                