# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, val: int):
            if not root:
                return 0
            
            cur = root.val >= val
            left = dfs(root.left, max(root.val, val))
            right = dfs(root.right, max(root.val, val))

            return cur + left + right
        
        return dfs(root, -float('inf'))