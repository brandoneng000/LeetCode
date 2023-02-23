# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # result = []
        # def traverse(root: Optional[TreeNode]) -> None:
        #     if root:
        #         result.append(root.val)
        #         traverse(root.left)
        #         traverse(root.right)
        
        # traverse(root)
        # return result    

        result = []
        right = []

        while root:
            result.append(root.val)
            if root.right:
                right.append(root.right)
            if root.left:
                root = root.left
            elif right:
                root = right.pop()
            else:
                break
            
        
        return result