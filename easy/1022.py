from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        res = 0

        while q:
            size = len(q)

            for _ in range(size):
                node, val = q.popleft()
                val = val * 2 + node.val
                
                if not node.left and not node.right:
                    res += val
                
                if node.left:
                    q.append((node.left, val))
                
                if node.right:
                    q.append((node.right, val))

        return res

    # def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
    #     def dfs(root: TreeNode, val: int = 0):
    #         if not root:
    #             return 0
            
    #         val = val * 2 + root.val
    #         if root.left == root.right:
    #             return val
    #         return dfs(root.left, val) + dfs(root.right, val)
        
    #     return dfs(root, 0)