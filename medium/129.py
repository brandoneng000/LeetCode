from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # self.num = 0
        # def dfs(root: TreeNode) -> int:
        #     self.num = self.num * 10 + root.val
        #     if not root.left and not root.right:
        #         val = self.num
        #         self.num //= 10
        #         return val
            
        #     val = 0
            
        #     if root.left:
        #         val += dfs(root.left)
            
        #     if root.right:
        #         val += dfs(root.right)
            
        #     self.num //= 10
        #     return val

        # return dfs(root)
        if not root: return 0
        stack = [(root, 0)]
        node = None
        cur_level = 0
        res = 0
        val = 0
        while stack or node:
            if node:
                print(node.val, cur_level)
                val = val * 10 + node.val
                if not node.left and not node.right:
                    res += val
                cur_level += 1
                if node.right:
                    stack.append((node.right, cur_level))
                node = node.left
            elif stack:
                node, level = stack.pop()
                while cur_level > level:
                    cur_level -= 1
                    val //= 10

        return res
