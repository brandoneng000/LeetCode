from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # linked_list_dict = set()

        # while head and head not in linked_list_dict:
        #     linked_list_dict.add(head)
        #     head = head.next
        
        # return head
        # slow, fast = head, head

        # while slow and fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if fast == slow:
        #         break
        
        # if not fast or not fast.next:
        #     return None
        
        # temp = head

        # while True:
        #     if temp == fast:
        #         return fast
        #     if fast == slow:
        #         temp = temp.next
        #     fast = fast.next
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else:
            return None

        while head != slow:
            head, slow = head.next, slow.next
        
        return head
            

