from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0

        while q:
            if level % 2:
                vals = [node.val for node in q][::-1]

                for node, num in zip(q, vals):
                    node.val = num
            
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            level += 1


        return root
    
    # def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     def dfs(node1: TreeNode, node2: TreeNode, level: int):
    #         if not node1 or not node2:
    #             return
            
    #         if level % 2:
    #             node1.val, node2.val = node2.val, node1.val
            
    #         dfs(node1.left, node2.right, level + 1)
    #         dfs(node1.right, node2.left, level + 1)
        
    #     dfs(root.left, root.right, 1)
    #     return root


    # def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     q = deque([root])
    #     level = 0

    #     while q:
    #         size = len(q)
    #         vals = [node.val for node in q]
    #         if level % 2:
    #             vals = vals[::-1]

    #         for i in range(size):
    #             node = q.popleft()
    #             node.val = vals[i]
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)

    #         level += 1
        
    #     return root