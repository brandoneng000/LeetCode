from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for j in range(n)] for i in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = 0, 0
        cur_dir = 0
        dr, dc = directions[cur_dir]

        while head:
            res[r][c] = head.val
            
            if 0 <= r + dr < m and 0 <= c + dc < n and res[r + dr][c + dc] == -1:
                pass
            else:
                cur_dir = (cur_dir + 1) % 4
                dr, dc = directions[cur_dir]

            r += dr
            c += dc

            head = head.next

        return res