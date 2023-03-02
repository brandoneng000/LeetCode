from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # stack = [root]
        # cur_node = TreeNode()

        # while stack:
        #     cur_node = stack.pop(0)
        #     if cur_node.val == val:
        #         return cur_node
        #     if cur_node.left:
        #         stack.append(cur_node.left)
        #     if cur_node.right:
        #         stack.append(cur_node.right)
        
        # return None
        cur_node = root

        while cur_node:
            if cur_node.val > val:
                cur_node = cur_node.left
            elif cur_node.val < val:
                cur_node = cur_node.right
            else:
                return cur_node

        return None