from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow and fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        return slow == fast

    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     if not head or not head.next:
    #         return False
    #     else:
    #         slow = head
    #         fast = head.next

    #     while slow is not fast:
    #         slow = slow.next
    #         fast = fast.next
    #         if not slow or not fast:
    #             return False
    #         fast = fast.next
    #         if not fast:
    #             return False
        
    #     return True