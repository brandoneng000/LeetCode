from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev_link_list(prev: ListNode, size: int):
            start = prev.next
            then = start.next
            end = start

            for _ in range(size - 1):
                start.next = then.next
                then.next = prev.next
                prev.next = then
                then = start.next
            
            return end
        
        res = cur = head
        group = 1
        count = 1
        connector = None

        while cur:
            if group == count or not cur.next:
                if count % 2 == 0:
                    cur = rev_link_list(connector, count)
                connector = cur
                group += 1
                count = 0
            
            count += 1
            cur = cur.next

        return res