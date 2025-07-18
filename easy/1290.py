# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        bits = []

        while cur:
            bits.append(str(cur.val))
            cur = cur.next
        
        return int(''.join(bits), 2)



    # def getDecimalValue(self, head: ListNode) -> int:
    #     result = 0

    #     while head:
    #         result <<= 1
    #         result += head.val
    #         head = head.next
        
    #     return result