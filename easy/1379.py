# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # cur_node = cloned
        # stack = []

        # while cur_node or stack:
        #     if cur_node:
        #         stack.append(cur_node)
        #         cur_node = cur_node.left
        #     else:
        #         cur_node = stack.pop()
        #         if cur_node.val == target.val:
        #             return cur_node
        #         cur_node = cur_node.right
        
        # return None

        node_o, node_c = original, cloned
        stack_o, stack_c = [], []
        while node_o or stack_o:
            if node_o:
                stack_o.append(node_o)
                stack_c.append(node_c)
                node_o = node_o.left
                node_c = node_c.left
            else:
                node_o = stack_o.pop()
                node_c = stack_c.pop()
                if node_o == target:
                    return node_c
                node_o = node_o.right
                node_c = node_c.right
        
        return None