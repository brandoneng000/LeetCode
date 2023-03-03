from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder_index = 0

        # def array_to_tree(left: int, right: int) -> TreeNode:
        #     nonlocal preorder_index
        #     if left > right:
        #         return None
            
        #     root_val = preorder[preorder_index]
        #     root = TreeNode(root_val)

        #     preorder_index += 1

        #     root.left = array_to_tree(left, inorder_map[root_val] - 1)
        #     root.right = array_to_tree(inorder_map[root_val] + 1, right)

        #     return root

        # inorder_map = {}

        # for index, val in enumerate(inorder):
        #     inorder_map[val] = index
        
        # return array_to_tree(0, len(preorder) - 1)
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root