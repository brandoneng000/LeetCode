from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # self.pre_order = []
        # def dfs(root: 'Node'):
        #     if not root:
        #         return
            
        #     self.pre_order.append(root.val)
        #     for child in root.children:
        #         dfs(child)
        
        # dfs(root)
        # return self.pre_order
        if not root:
            return []
        pre_order = []
        stack = [root]

        while stack:
            node = stack.pop()
            pre_order.append(node.val)
            if node.children:
                stack.extend(node.children[::-1])
        
        return pre_order
