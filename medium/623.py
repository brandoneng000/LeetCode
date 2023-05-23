from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        
        prev = collections.deque([])
        q = collections.deque([root])
        temp = collections.deque([])
        level = 1

        while q:
            node = q.popleft()
            if level == depth - 1:
                prev.append(node)
            
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            
            if not q and temp:
                q = temp.copy()
                temp = collections.deque([])
                level += 1
                if level == depth:
                    break
        
        while prev:
            node = prev.popleft()
            left = TreeNode(val, node.left)
            right = TreeNode(val, None, node.right)
            node.left = left
            node.right = right

        return root