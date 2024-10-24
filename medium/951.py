from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    #     q1 = deque([root1])
    #     q2 = deque([root2])

    #     while q1 and q2:
    #         node1 = q1.popleft()
    #         node2 = q2.popleft()

    #         if not node1 and not node2:
    #             continue
    #         elif not node1 or not node2 or node1.val != node2.val:
    #             return False
            
    #         if (not node1.left and not node2.left) or node1.left and node2.left and node1.left.val == node2.left.val:
    #             q1.extend([node1.left, node1.right])
    #         else:
    #             q1.extend([node1.right, node1.left])
            
    #         q2.extend([node2.left, node2.right])

    #     return not q1 and not q2

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)) or \
                (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))