from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        stack = []
        cur_node = root
        val = root.val

        while cur_node or stack:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            elif stack:
                cur_node = stack.pop()
                if cur_node.val != val:
                    return False
                cur_node = cur_node.right

        return True
        # val = root.val
        # def dfs(root: TreeNode) -> bool:
        #     if not root:
        #         return True

        #     return root.val == val and dfs(root.left) and dfs(root.right)
        
        # return dfs(root)
            
