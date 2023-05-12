from typing import Optional
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ""
        res = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(str(-1))
        
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data: return None

        data_q = collections.deque(data.split(','))
        head = root = TreeNode(int(data_q.popleft()))
        q = collections.deque([root])
        while data_q:
            node = q.popleft()
            left = int(data_q.popleft())
            right = int(data_q.popleft())
            if left == -1:
                node.left = None
            else:
                node.left = TreeNode(left)
                q.append(node.left)
            
            if right == -1:
                node.right = None
            else:
                node.right = TreeNode(right)
                q.append(node.right)

        return head
