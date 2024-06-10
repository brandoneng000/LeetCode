from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def swaps(arr: List[int]):
            n = len(arr)
            pos = [*enumerate(arr)]
            pos.sort(key=lambda x: x[1])

            visited = set()
            res = 0

            for i in range(n):
                if i in visited or pos[i][0] == i:
                    continue
                cycle = 0
                j = i

                while j not in visited:
                    visited.add(j)
                    j = pos[j][0]
                    cycle += 1
                
                if cycle > 0:
                    res += cycle - 1

            return res

        q = deque([root])
        res = 0

        while q:
            res += swaps([node.val for node in q])
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res
