from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        prev = root

        while q:
            node = q.popleft()
            
            if node:
                if not prev:
                    return False
                q.append(node.left)
                q.append(node.right)
            prev = node
        
        return True

    # def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    #     q = collections.deque([root])
    #     level = 0
    #     end = False

    #     while q:
    #         size = len(q)
    #         level += 1
    #         for _ in range(size):
    #             node = q.popleft()

    #             if end and (node.left or node.right):
    #                 return False
    #             elif end:
    #                 continue

    #             if not node.left and node.right:
    #                 return False

    #             if node.left:
    #                 q.append(node.left)
                
    #             if node.right:
    #                 q.append(node.right)
                
    #             if not node.left or not node.right:
    #                 end = True
            
    #         if 2 ** level != len(q):
    #             break
        
    #     for node in q:
    #         if node.left or node.right:
    #             return False
        
    #     return True
