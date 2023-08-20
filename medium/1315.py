# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0

        def dfs(root: TreeNode, parent: TreeNode, grandparent: TreeNode):
            if not root:
                return
            
            if grandparent and grandparent.val % 2 == 0:
                self.total += root.val

            dfs(root.left, root, parent)
            dfs(root.right, root, parent)
        
        dfs(root, None, None)
        return self.total

    # def sumEvenGrandparent(self, root: TreeNode) -> int:
    #     self.total = 0

    #     def dfs(root: TreeNode, cur_level: int, grandparent: set):
    #         if not root:
    #             return
            
    #         if cur_level in grandparent:
    #             self.total += root.val
            
    #         if root.val % 2 == 0:
    #             grandparent.add(cur_level + 2)
    #         else:
    #             grandparent.discard(cur_level + 2)
            
    #         dfs(root.left, cur_level + 1, grandparent)
    #         dfs(root.right, cur_level + 1, grandparent)
        
    #     dfs(root, 0, set())
    #     return self.total