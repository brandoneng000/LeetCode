from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: TreeNode):
            if not root:
                return [0, None]
            
            left_depth, left = dfs(root.left)
            right_depth, right = dfs(root.right)

            if left_depth > right_depth:
                return left_depth + 1, left
            elif left_depth < right_depth:
                return right_depth + 1, right
            
            return left_depth + 1, root
        
        return dfs(root)[1]

    # def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     self.res = None
    #     self.max_depth = 0

    #     def dfs(root: TreeNode, depth: int):
    #         if not root:
    #             return depth - 1
            
    #         self.max_depth = max(self.max_depth, depth)
    #         left = dfs(root.left, depth + 1)
    #         right = dfs(root.right, depth + 1)

    #         if left == right == self.max_depth:
    #             self.res = root
            
    #         return max(left, right)
        
    #     dfs(root, 0)
    #     return self.res