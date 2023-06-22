from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder: List[int], postorder: List[int]):
            if preorder and postorder:
                root = preorder.pop(0)
                postorder.pop()
                index = postorder.index(preorder[0]) + 1 if postorder else 0
                return TreeNode(root, helper(preorder[:index], postorder[:index]), helper(preorder[index:], postorder[index:]))
        
        return helper(preorder, postorder)
            
