from typing import List, Optional
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def height(root: TreeNode):
            if not root:
                return -1
            
            if root in levels:
                return levels[root]

            h = 1 + max(height(root.left), height(root.right))
            levels[root] = h
            return h

        def dfs(root: TreeNode, level: int, max_val: int):
            if not root:
                return
            
            res_map[root.val] = max_val
            dfs(root.left, level + 1, max(max_val, level + 1 + height(root.right)))
            dfs(root.right, level + 1, max(max_val, level + 1 + height(root.left)))

        res_map = {}
        levels = {}

        dfs(root, 0, 0)

        return [res_map[q] for q in queries]
