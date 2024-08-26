from typing import List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # def postorder(self, root: 'Node') -> List[int]:
    #     q = deque([root])
    #     res = []

    #     while q:
    #         size = len(q)

    #         for _ in range(size):
    #             node = q.popleft()

    #             if node:
    #                 res.append(node.val)
    #                 q.extendleft(node.children)
        
    #     return res[::-1]


    # def postorder(self, root: 'Node') -> List[int]:
    #     self.post_order = []

    #     def dfs(root: 'Node'):
    #         if not root:
    #             return
            
    #         for child in root.children:
    #             dfs(child)
    #         self.post_order.append(root.val)
        
    #     dfs(root)
    #     return self.post_order
    
    def postorder(self, root: 'Node') -> List[int]:
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(node.children)

        return res[::-1]
