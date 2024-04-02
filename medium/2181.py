from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = cur = ListNode()

        while head:
            if head.val == 0:
                if head.next:
                    cur.next = ListNode()
                    cur = cur.next
            else:
                cur.val += head.val
            
            head = head.next

        return res.next