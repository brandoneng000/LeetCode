# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.cur = 0

        def dfs(root: TreeNode):
            if not root:
                return None
            
            right = dfs(root.right)
            self.cur += root.val
            node = TreeNode(self.cur, None, right)
            node.left = dfs(root.left)

            return node
        
        return dfs(root)