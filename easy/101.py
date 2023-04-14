from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # def compare_trees(left: TreeNode, right: TreeNode):
        #     if not left and not right:
        #         return True
        #     elif not left or not right:
        #         return False

        #     if left.val == right.val:
        #         return compare_trees(left.left, right.right) and compare_trees(left.right, right.left)
        #     else:
        #         return False
            
        # return compare_trees(root.left, root.right)
        
        if not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False

        left_stack = [root.left]
        right_stack = [root.right]

        while left_stack or right_stack:
            if not left_stack or not right_stack:
                return False
            
            left = left_stack.pop()
            right = right_stack.pop()

            if not left and not right:
                pass
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False

            if left and right:
                left_stack.append(left.left)
                right_stack.append(right.right)

                left_stack.append(right.left)
                right_stack.append(left.right)

        return True