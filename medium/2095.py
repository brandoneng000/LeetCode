from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        fast = head.next.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next

        return head

    # def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     slow = fast = head
    #     prev = None

    #     while fast and fast.next:
    #         fast = fast.next.next
    #         prev = slow
    #         slow = slow.next
            
    #     if prev:
    #         prev.next = slow.next
    #     if not prev:
    #         return None

    #     return head