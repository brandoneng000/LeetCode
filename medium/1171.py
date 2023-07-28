from typing import Optional
import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = {}
        prefix = 0
        prefix_sum[0] = temp = ListNode(0)
        temp.next = head

        while head:
            prefix += head.val
            prefix_sum[prefix] = head
            head = head.next

        head = temp
        prefix = 0

        while head:
            prefix += head.val
            head.next = prefix_sum[prefix].next
            head = head.next
        
        return temp.next
        