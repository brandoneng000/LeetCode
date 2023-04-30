from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        odd_start = odd = head.next
        even = head
        res = even

        while even.next and even.next.next:
            store_even_next = even.next
            even.next = even.next.next
            even = even.next

            store_even_next.next = None
            odd.next = store_even_next
            odd = odd.next

        if even.next:
            temp = even.next
            even.next = None
            odd.next = temp
            odd = odd.next

        odd.next = None
        even.next = odd_start
        return res