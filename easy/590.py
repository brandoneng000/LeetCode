from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # self.post_order = []

        # def dfs(root: 'Node'):
        #     if not root:
        #         return
            
        #     for child in root.children:
        #         dfs(child)
        #     self.post_order.append(root.val)
        
        # dfs(root)
        # return self.post_order
        if not root:
            return []
        post_order = []
        stack = [root]
        while stack:
            node = stack.pop()
            post_order.append(node.val)
            if node.children:
                stack.extend(node.children)

        return post_order[::-1]
