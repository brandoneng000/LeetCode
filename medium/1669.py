# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        res = cur = list1
        end_b = list1

        for _ in range(b + 1):
            end_b = end_b.next
        
        for _ in range(a - 1):
            cur = cur.next
        
        cur.next = list2

        while cur.next:
            cur = cur.next
        
        cur.next = end_b

        return res