from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.height_tree(root)
        width = 2 ** height - 1
        self.res = [["" for i in range(width)] for j in range(height)]
        self.update_print(root, 0, 0, width - 1)
        return self.res
    
    def update_print(self, node, level, left, right):
        if not node:
            return
        middle = (left + right) // 2
        self.res[level][middle] = str(node.val)
        self.update_print(node.left, level + 1, left, middle - 1)
        self.update_print(node.right, level + 1, middle + 1, right)

    def height_tree(self, root: TreeNode):
        if not root:
            return 0
        
        return max(self.height_tree(root.left), self.height_tree(root.right)) + 1
