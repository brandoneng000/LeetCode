from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = pre = ListNode()
        temp.next = head
        while head and head.next:
            store = head.next
            head.next = store.next
            store.next = head
            pre.next = store
            head = head.next
            pre = store.next
        
        return temp.next
        