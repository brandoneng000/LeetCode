from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_lca(root: TreeNode):
            if not root or root.val == startValue or root.val == destValue:
                return root
            left = find_lca(root.left)
            right = find_lca(root.right)

            return root if left and right else left or right
        
        root = find_lca(root)

        start_path = dest_path = ""
        stack = [(root, "")]

        while stack:
            node, path = stack.pop()

            if node.val == startValue:
                start_path = path
            if node.val == destValue:
                dest_path = path
            
            if node.left:
                stack.append((node.left, path + "L"))
            if node.right:
                stack.append((node.right, path + "R"))
        
        return "U" * len(start_path) + dest_path

    # def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    #     def find_path(root: TreeNode, goal: int, path: str):
    #         if not root:
    #             return "X"
    #         if root.val == goal:
    #             return path
            
    #         left = find_path(root.left, goal, path + 'L')
    #         if left != 'X':
    #             return left
            
    #         right = find_path(root.right, goal, path + 'R')
    #         if right != 'X':
    #             return right
            
    #         return 'X'
            
        
    #     start_path = find_path(root, startValue, "")
    #     dest_path = find_path(root, destValue, "")

    #     if not start_path:
    #         return dest_path
    #     elif not dest_path:
    #         return "U" * len(start_path)
    #     else:
    #         res = []
    #         index = 0

    #         while index < len(start_path) and index < len(dest_path) and start_path[index] == dest_path[index]:
    #             index += 1
            
    #         i = index

    #         while i < len(start_path):
    #             res.append("U")
    #             i += 1
            
    #         return "".join(res) + dest_path[index:]
