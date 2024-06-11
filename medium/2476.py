from typing import List, Optional
from bisect import bisect_left

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def dfs(root: TreeNode):
            if not root:
                return
            
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)

        nums = []
        dfs(root)
        n = len(nums)
        res = []

        for goal in queries:
            index = bisect_left(nums, goal)
            if index < n and nums[index] == goal:
                res.append([goal, goal])
            else:
                if index == 0:
                    res.append([-1, nums[0]])
                elif index == n:
                    res.append([nums[-1], -1])
                else:
                    res.append([nums[index - 1], nums[index]])

        return res