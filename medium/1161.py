from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        children = 1
        level = 1
        total = 0
        res = (root.val, 1)

        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            children -= 1
            total += node.val

            if children == 0:
                if res[0] < total:
                    res = (total, level)
                total = 0
                level += 1
                children = len(q)
        
        return res[1]