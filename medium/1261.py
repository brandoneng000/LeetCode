from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.tree_vals = set()
        q = deque([[root, 0]])

        while q:
            node, val = q.popleft()
            self.tree_vals.add(val)

            if node.left:
                q.append([node.left, val * 2 + 1])
            
            if node.right:
                q.append([node.right, val * 2 + 2])


    def find(self, target: int) -> bool:
        return target in self.tree_vals
        
# class FindElements:
#     def __init__(self, root: Optional[TreeNode]):
#         def dfs(root: TreeNode, expected_val: int):
#             if not root:
#                 return
            
#             self.tree_vals.add(expected_val)
#             dfs(root.left, expected_val * 2 + 1)
#             dfs(root.right, expected_val * 2 + 2)

#         self.tree_vals = set()
#         dfs(root, 0)

#     def find(self, target: int) -> bool:
#         return target in self.tree_vals

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)