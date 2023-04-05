from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # def get_size(root: TreeNode) -> int:
        #     if not root.right and not root.left:
        #         return 1
        #     left = right = 0
        #     if root.left:
        #         left = get_size(root.left)
        #     if root.right:
        #         right = get_size(root.right)
        #     return left + right + 1
        
        # while True:
        #     left = 0
        #     if root.left:
        #         left = get_size(root.left)
            
        #     if left == k - 1:
        #         return root.val
        #     elif left > k - 1:
        #         root = root.left
        #     else:
        #         root = root.right
        #         k -= left + 1
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right