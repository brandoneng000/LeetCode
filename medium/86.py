from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res = temp = ListNode(-101, next=head)
        store = greater = ListNode()
        prev = ListNode()

        while temp:
            if temp.val < x:
                prev = temp
            else:
                greater.next = temp
                greater = greater.next
                
                prev.next = temp.next
            temp = temp.next

        greater.next = None
        prev.next = store.next
        return res.next