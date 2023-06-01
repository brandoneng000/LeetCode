from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        size = 0
        res = []
        while temp:
            temp = temp.next
            size += 1
        
        split_size = size // k
        split_remainder = size % k
        temp = head
        for i in range(k):
            temp_size = split_size
            res.append(temp)
            for j in range(temp_size + (i < split_remainder) - 1):
                temp = temp.next
            if temp:
                next = temp.next
                temp.next = None
                temp = next
        return res