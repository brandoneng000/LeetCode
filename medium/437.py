from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0

        def dfs(root: TreeNode, target: int, include: bool):
            if not root:
                return
            
            if include:
                if target - root.val == 0:
                    self.res += 1
                dfs(root.left, target - root.val, True)
                dfs(root.right, target - root.val, True)
            else:
                dfs(root.left, target, True)
                dfs(root.right, target, True)
                dfs(root.left, target, False)
                dfs(root.right, target, False)
        
        dfs(root, targetSum, True)
        dfs(root, targetSum, False)
        return self.res