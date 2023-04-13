from typing import Optional
import collections

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        temp = root
        queue = collections.deque([temp])
        children = 1
        prev = None

        while queue:
            node = queue.popleft()
            children -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if not prev:
                prev = node
            else:
                prev.next = node
                prev = prev.next

            if not children:
                prev.next = None
                prev = None
                children = len(queue)
        
        return root

