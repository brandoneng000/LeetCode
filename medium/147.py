from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = temp = ListNode(-5001)

        while head:
            cur = head
            head = head.next
            insert = temp
            while insert and insert.val < cur.val:
                prev = insert
                insert = insert.next
            next = prev.next
            prev.next = cur
            cur.next = next

        return res.next

