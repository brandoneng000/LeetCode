from typing import Optional, List
from collections import defaultdict, deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    #     def dfs(root: TreeNode, level: int):
    #         if not root:
    #             return
            
    #         self.max_level = max(self.max_level, level)
    #         max_val[level] = max(max_val[level], root.val)
    #         dfs(root.left, level + 1)
    #         dfs(root.right, level + 1)

    #     max_val = defaultdict(lambda: -float('inf'))
    #     self.max_level = -1
    #     dfs(root, 0)

    #     return [max_val[level] for level in range(self.max_level + 1)]

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([TreeNode(0, root)])
        next = deque([])
        res = []
        while q:
            node = q.popleft()
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
            
            if not q and next:
                res.append(max([n.val for n in next]))
                q = next
                next = deque([])
        
        return res