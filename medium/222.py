from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # if not root: return 0
        # res = 0
        # children = 1
        # queue = collections.deque([root])

        # while queue:
        #     node = queue.popleft()
        #     res += 1
        #     children -= 1
            
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
            
        #     if not node.left or not node.right:
        #         res += len(queue) - children
        #         break

        #     if children == 0:
        #         children = len(queue)
            
        # return res

        def depth(root: TreeNode):
            if not root:
                return 0
            return 1 + depth(root.left)
        
        if not root: return 0
        left = depth(root.left)
        right = depth(root.right)
        if left == right:
            return 2 ** left + self.countNodes(root.right)
        else:
            return 2 ** right + self.countNodes(root.left)
