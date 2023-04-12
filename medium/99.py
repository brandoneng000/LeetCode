from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root: TreeNode) -> list:
            if not root.left and not root.right:
                return [root]
            
            vals = []
            if root.left:
                vals += dfs(root.left)
            
            vals += [root]

            if root.right:
                vals += dfs(root.right)
            
            return vals
        
        in_order = dfs(root)
        sorted_order = sorted(in_order, key=lambda x: x.val)
        first, second = TreeNode(-1), TreeNode(-2)

        for index in range(len(in_order)):
            if in_order[index] != sorted_order[index]:
                if second.val == -1:
                    second = in_order[index]
                    break
                if first.val == -1:
                    first = in_order[index]
                    second = TreeNode(-1)
                
        temp = first.val
        first.val = second.val
        second.val = temp