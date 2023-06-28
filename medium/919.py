from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = collections.deque([root])
        self.cur = None
        self.bfs()

    def insert(self, val: int) -> int:
        root = self.cur.val
        if not self.cur.left:
            self.cur.left = TreeNode(val)
            self.q.append(self.cur.left)
            return root
        
        if not self.cur.right:
            self.cur.right = TreeNode(val)
            self.q.append(self.cur.right)
            self.bfs()
            return root


    def get_root(self) -> Optional[TreeNode]:
        return self.root

    def bfs(self):
        while self.q:
            self.cur = self.q.popleft()
            if self.cur.left:
                self.q.append(self.cur.left)
            else:
                break

            if self.cur.right:
                self.q.append(self.cur.right)
            else:
                break

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()