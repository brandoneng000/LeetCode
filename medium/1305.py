from typing import List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(vals: collections.deque[int], root: TreeNode):
            if root:
                dfs(vals, root.left)
                vals.append(root.val)
                dfs(vals, root.right)
        
        vals1, vals2 = collections.deque(), collections.deque()
        res = []
        dfs(vals1, root1)
        dfs(vals2, root2)

        while vals1 or vals2:
            if not vals1:
                res.append(vals2.popleft())
            elif not vals2:
                res.append(vals1.popleft())
            elif vals1[0] <= vals2[0]:
                res.append(vals1.popleft())
            else:
                res.append(vals2.popleft())

        return res
    
    # def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    #     def dfs(vals: List[int], root: TreeNode):
    #         if root:
    #             vals.append(root.val)
    #             dfs(vals, root.left)
    #             dfs(vals, root.right)
        
    #     vals1, vals2 = [], []
    #     dfs(vals1, root1)
    #     dfs(vals2, root2)

    #     return sorted(vals1 + vals2)
