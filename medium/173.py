from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.traverse_left(root)

    def next(self) -> int:
        if self.stack:
            node = self.stack.pop()
            if node.right:
                self.traverse_left(node.right)
        
        return node.val
    
    def traverse_left(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left 

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()