from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []

        while head:
            while stack and stack[-1][0] < head.val:
                _, index = stack.pop()
                res[index] = head.val
            stack.append((head.val, len(res)))
            res.append(0)
            head = head.next
        
        return res