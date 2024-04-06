from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parents = set()
        children = set()
        tree = {}

        for parent, child, left, in descriptions:
            if parent not in tree:
                tree[parent] = TreeNode(parent)
            if child not in tree:
                tree[child] = TreeNode(child)
            
            parents.add(parent)
            children.add(child)

            if left:
                tree[parent].left = tree[child]
            else:
                tree[parent].right = tree[child]

        return tree[(parents - children).pop()]