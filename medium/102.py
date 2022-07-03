from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # vals = []

        # def bfs(root: TreeNode, level: int):
        #     if not root:
        #         return
            
        #     if len(vals) <= level:
        #         vals.append([])
            
        #     vals[level].append(root.val)
        #     bfs(root.left, level + 1)
        #     bfs(root.right, level + 1)
        
        # bfs(root, 0)
        # return vals
        if not root:
            return None

        res = []
        queue = []
        queue.append(root)

        while len(queue) > 0:
            cur = []
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur)
        
        return res
            