from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def in_order(root: TreeNode):
            if not root:
                return
            
            in_order(root.left)
            vals.append(root.val)
            in_order(root.right)
        
        def generate_tree(vals: List[int]):
            if not vals:
                return None
            
            middle_index = len(vals) // 2
            root = TreeNode(vals[middle_index])
            root.left = generate_tree(vals[:middle_index - 1])
            root.right = generate_tree(vals[middle_index + 1:])

            return root

        vals = []
        in_order(root)
        return generate_tree(vals)