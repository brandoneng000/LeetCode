from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = res = ListNode(next=head)
        fast_forward = cur = head
        left -= 1
        right -= 1

        def reverse_linked_list(head: ListNode):
            prev = None
            cur = head
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            
            return prev

        while left < right:
            fast_forward = fast_forward.next
            right -= 1

        while left:
            cur = cur.next
            prev = prev.next
            fast_forward = fast_forward.next
            left -= 1
        
        ff_next = fast_forward.next
        fast_forward.next = None
        reverse = reverse_linked_list(cur)
        prev.next = reverse
        while reverse.next:
            reverse = reverse.next

        reverse.next = ff_next
        
        return res.next