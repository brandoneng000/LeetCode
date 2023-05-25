from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        val = max(nums)
        index = nums.index(val)
        node = TreeNode(val)

        left = self.constructMaximumBinaryTree(nums[:index])
        right = self.constructMaximumBinaryTree(nums[index + 1:])
        node.left = left
        node.right = right

        return node