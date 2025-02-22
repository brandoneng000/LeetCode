from typing import Optional, List
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        q = deque()
        dashes = 0
        val = 0

        for cur in traversal:
            if cur == '-' and val == 0:
                dashes += 1
            elif cur == '-':
                q.append([dashes, val])
                val = 0
                dashes = 1
            else:
                val *= 10
                val += int(cur)
        
        q.append([dashes, val])
        levels = defaultdict(list)
        depth, val = q.popleft()
        levels[0].append(TreeNode(val))

        while q:
            depth, val = q.popleft()
            node = TreeNode(val)
            cur = levels[depth - 1][-1]
            levels[depth].append(node)

            if not cur.left:
                cur.left = node
            elif not cur.right:
                cur.right = node


        return levels[0][0]