from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.res = []
        self.path = []

        def dfs(root: TreeNode, target_sum: int):
            if target_sum - root.val == 0 and not root.left and not root.right:
                self.path.append(root.val)
                self.res.append(self.path.copy())
                self.path.pop()
                return
            
            self.path.append(root.val)
            if root.left:
                dfs(root.left, target_sum - root.val)
            if root.right:
                dfs(root.right, target_sum - root.val)
            self.path.pop()
        
        dfs(root, targetSum)
        return self.res


