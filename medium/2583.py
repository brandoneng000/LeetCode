from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        nums = []

        while q:
            cur = 0
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                cur += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            nums.append(cur)
        
        return sorted(nums, reverse=True)[k - 1] if len(nums) >= k else -1