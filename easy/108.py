from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def branch(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = branch(left, mid - 1)
            node.right = branch(mid + 1, right)
            return node
        return branch(0, len(nums) - 1)
