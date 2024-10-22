from typing import Optional
from collections import deque, Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root: TreeNode, level: int):
            if not root:
                return
            
            self.levels = max(self.levels, level)
            level_sum[level] += root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        level_sum = Counter()
        self.levels = 0
        dfs(root, 1)
        
        return level_sum.most_common()[k - 1][1] if self.levels >= k else -1



    # def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
    #     q = deque([root])
    #     nums = []

    #     while q:
    #         cur = 0
    #         size = len(q)

    #         for _ in range(size):
    #             node = q.popleft()
    #             cur += node.val
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         nums.append(cur)
        
    #     return sorted(nums, reverse=True)[k - 1] if len(nums) >= k else -1