from typing import Optional
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs_calc(root: TreeNode, parent: TreeNode, level: int):
            if not root:
                return
            
            parent_sums[parent] += root.val
            level_sums[level] += root.val
            dfs_calc(root.left, root, level + 1)
            dfs_calc(root.right, root, level + 1)

        def dfs_replace(root: TreeNode, parent: TreeNode, level: int):
            if not root:
                return
            
            dfs_replace(root.left, root, level + 1)
            dfs_replace(root.right, root, level + 1)

            root.val = level_sums[level] - parent_sums[parent]
        
        level_sums = defaultdict(int)
        parent_sums = defaultdict(int)
        temp = TreeNode()
        dfs_calc(root, temp, 0)
        dfs_replace(root, temp, 0)

        return root


    # def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     cur_level_sum = root.val
    #     q = deque([root])

    #     while q:
    #         next_level = []
    #         next_level_sum = 0

    #         for node in q:
    #             node.val = cur_level_sum - node.val
                
    #             for child in node.left, node.right:
    #                 if child:
    #                     next_level.append(child)
    #                     next_level_sum += child.val
                
    #             if node.left and node.right:
    #                 total = node.left.val + node.right.val
    #                 node.left.val = node.right.val = total
            
    #         q = next_level
    #         cur_level_sum = next_level_sum
        
    #     return root