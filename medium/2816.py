from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev_link_list(head: ListNode):
            prev = None

            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            
            return prev
        
        head = res = rev_link_list(head)
        prev = None
        carry = 0

        while head:
            carry, head.val = divmod(head.val * 2 + carry, 10)
            prev = head
            head = head.next
        
        if carry:
            prev.next = ListNode(carry)
        
        return rev_link_list(res)