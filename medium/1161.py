from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, level: int):
            if not node:
                return
            
            levels[level] = levels.get(level, 0) + node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        levels = {}
        dfs(root, 1)
        res = 1
        max_sum = levels[1]

        for l in levels:
            if levels[l] > max_sum:
                res = l
                max_sum = levels[l]
        
        return res


    # def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    #     q = collections.deque([root])
    #     children = 1
    #     level = 1
    #     total = 0
    #     res = (root.val, 1)

    #     while q:
    #         node = q.popleft()
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #         children -= 1
    #         total += node.val

    #         if children == 0:
    #             if res[0] < total:
    #                 res = (total, level)
    #             total = 0
    #             level += 1
    #             children = len(q)
        
    #     return res[1]