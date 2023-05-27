from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([(root, 0)])
        res = 1

        while q:
            size = len(q)
            left = q[0][1]

            for i in range(size):
                node, node_index = q.popleft()
                if node.left:
                    q.append((node.left, 2 * node_index))
                if node.right:
                    q.append((node.right, 2 * node_index + 1))
            
            res = max(res, node_index - left + 1)

        return res