from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        delete_nodes = set(to_delete)
        res = [root] if root.val not in delete_nodes else []

        q = deque([[root, TreeNode(left=root), True]])

        while q:
            node, parent, left = q.popleft()

            if node.val in delete_nodes:
                if left:
                    parent.left = None
                else:
                    parent.right = None
                if node.left and node.left.val not in delete_nodes:
                    res.append(node.left)
                if node.right and node.right.val not in delete_nodes:
                    res.append(node.right)
            
            if node.left:
                q.append([node.left, node, True])
            if node.right:
                q.append([node.right, node, False])
        
        return res


    # def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    #     delete = set(to_delete)
    #     self.res = []

    #     def dfs(root: TreeNode):
    #         if not root:
    #             return None
            
    #         root.left = dfs(root.left)
    #         root.right = dfs(root.right)

    #         if root.val in delete:
    #             if root.left:
    #                 self.res.append(root.left)
    #             if root.right:
    #                 self.res.append(root.right)
    #             return None

    #         return root

    #     node = dfs(root)
    #     if node:
    #         self.res.append(node)
        
    #     return self.res