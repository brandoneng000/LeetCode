from collections import namedtuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
    #     def dfs(node: TreeNode):
    #         if not node:
    #             return res(None, 0)
            
    #         left = dfs(node.left)
    #         right = dfs(node.right)

    #         if left.dist > right.dist:
    #             return res(left.node, left.dist + 1)
    #         if left.dist < right.dist:
    #             return res(right.node, right.dist + 1)
            
    #         return res(node, left.dist + 1)
        
    #     res = namedtuple("Result", ("node", "dist"))
    #     return dfs(root).node
        

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.res = root
        self.max_depth = 0
        
        def dfs(root: TreeNode, depth: int):
            if not root:
                return depth
            
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)

            if left == right:
                if self.max_depth <= left:
                    self.res = root
                    self.max_depth = left
                return left

            return max(left, right)

        dfs(root, 0)
        return self.res