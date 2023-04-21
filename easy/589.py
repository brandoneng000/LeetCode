from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.in_order = []
        def dfs(root: 'Node'):
            if not root:
                return
            
            self.in_order.append(root.val)
            for child in root.children:
                dfs(child)
        
        dfs(root)
        return self.in_order