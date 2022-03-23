from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = store = ListNode(-1, head)
        cur = head

        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
            
        return store.next