from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        q = deque([["", root]])
        res = None

        while q:
            size = len(q)

            for _ in range(size):
                cur, node = q.popleft()
                cur = chr(node.val + ord('a')) + cur

                if not node.left and not node.right:
                    if not res:
                        res = cur
                    res = min(res, cur)
                
                if node.left:
                    q.append([cur, node.left])
                if node.right:
                    q.append([cur, node.right])
        
        return res


    # def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
    #     def dfs(root: TreeNode):
    #         if not root:
    #             return []
            
    #         letter = chr(root.val + ord('a'))
            
    #         if not root.left and not root.right:
    #             return [letter]
            
    #         left = dfs(root.left)
    #         right = dfs(root.right)

    #         return [letters + letter for letters in left + right]
        
    #     return min(dfs(root))