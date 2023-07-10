from typing import List, Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        left = []
        right = []
        for i in range(1, len(preorder)):
            if root.val > preorder[i]:
                left.append(preorder[i])
            else:
                right.append(preorder[i])
                
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)

        return root