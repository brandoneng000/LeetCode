from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
                
        return node.val

        
        # q = collections.deque([root])
        # next = collections.deque([])
        # res = []
        # while q:
        #     node = q.popleft()
        #     res.append(node.val)
        #     if node.left:
        #         next.append(node.left)
        #     if node.right:
        #         next.append(node.right)
            
        #     if not q and next:
        #         q = next.copy()
        #         next.clear()
        #         res.clear()
        
        # return res[0]