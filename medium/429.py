from typing import List
import collections

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        next_level = collections.deque()
        res = []
        cur_level = []

        while queue:
            node = queue.popleft()
            next_level.extend(node.children)
            cur_level.append(node.val)

            if not queue:
                queue = next_level
                next_level = collections.deque()
                res.append(cur_level.copy())
                cur_level = []
        

        return res

