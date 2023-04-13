from typing import Optional, List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        children = 1
        res = []
        temp = []

        while queue:
            node = queue.popleft()
            temp.append(node.val)
            children -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            if not children:
                children = len(queue)
                res.append(temp.copy())
                temp.clear()
        
        return reversed(res)