from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        size1, size2 = 0, 0
        temp1, temp2 = l1, l2
        prev = []

        while temp1 or temp2:
            if temp1:
                temp1 = temp1.next
                size1 += 1
            if temp2:
                temp2 = temp2.next
                size2 += 1
        
        if size1 >= size2:
            larger = res = ListNode(0, l1)
            temp = l2
        else:
            larger = res = ListNode(0, l2)
            temp = l1
            size1, size2 = size2, size1

        size1 += 1
        while size1 != size2:
            prev.append(larger)
            larger = larger.next
            size1 -= 1
        
        while larger and temp:
            larger.val += temp.val
            if larger.val >= 10:
                larger.val = larger.val % 10
                while prev:
                    node = prev.pop()
                    node.val += 1
                    if node.val >= 10:
                        node.val = node.val % 10
                    else:
                        prev.clear()
            
            prev.append(larger)
            larger = larger.next
            temp = temp.next

        return res if res.val != 0 else res.next
