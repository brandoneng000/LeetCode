from typing import Optional, List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([TreeNode(0, root)])
        next = collections.deque([])
        res = []
        while q:
            node = q.popleft()
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
            
            if not q and next:
                res.append(max([n.val for n in next]))
                q = next
                next = collections.deque([])
        
        return res