from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        temp1, temp2 = l1, l2

        while temp1 or temp2:
            if temp1:
                s1.append(str(temp1.val))
                temp1 = temp1.next
            if temp2:
                s2.append(str(temp2.val))
                temp2 = temp2.next
        
        val1, val2 = int("".join(s1)), int("".join(s2))
        total = str(val1 + val2)
        res = temp = ListNode()

        for val in total:
            temp.next = ListNode(int(val))
            temp = temp.next
        
        return res.next
        
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     s1, s2 = [], []
    #     temp1, temp2 = l1, l2

    #     while temp1 or temp2:
    #         if temp1:
    #             s1.append(temp1.val)
    #             temp1 = temp1.next
    #         if temp2:
    #             s2.append(temp2.val)
    #             temp2 = temp2.next
            
    #     s1, s2 = s1[::-1], s2[::-1]
    #     i1, i2 = 0, 0
    #     carry = 0
    #     total = []

    #     while i1 < len(s1) or i2 < len(s2):
    #         val1, val2 = 0, 0
    #         if i1 < len(s1):
    #             val1 = s1[i1]
    #             i1 += 1
    #         if i2 < len(s2):
    #             val2 = s2[i2]
    #             i2 += 1
    #         total_val = val1 + val2 + carry
    #         if total_val >= 10:
    #             total_val -= 10
    #             carry = 1
    #         else:
    #             carry = 0
    #         total.append(total_val)

    #     if carry:
    #         total.append(1)

    #     total = total[::-1]
    #     res = temp = ListNode()

    #     for val in total:
    #         temp.next = ListNode(val)
    #         temp = temp.next
        
    #     return res.next
            

    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     size1, size2 = 0, 0
    #     temp1, temp2 = l1, l2
    #     prev = []

    #     while temp1 or temp2:
    #         if temp1:
    #             temp1 = temp1.next
    #             size1 += 1
    #         if temp2:
    #             temp2 = temp2.next
    #             size2 += 1
        
    #     if size1 >= size2:
    #         larger = res = ListNode(0, l1)
    #         temp = l2
    #     else:
    #         larger = res = ListNode(0, l2)
    #         temp = l1
    #         size1, size2 = size2, size1

    #     size1 += 1
    #     while size1 != size2:
    #         prev.append(larger)
    #         larger = larger.next
    #         size1 -= 1
        
    #     while larger and temp:
    #         larger.val += temp.val
    #         if larger.val >= 10:
    #             larger.val = larger.val % 10
    #             while prev:
    #                 node = prev.pop()
    #                 node.val += 1
    #                 if node.val >= 10:
    #                     node.val = node.val % 10
    #                 else:
    #                     prev.clear()
            
    #         prev.append(larger)
    #         larger = larger.next
    #         temp = temp.next

    #     return res if res.val != 0 else res.next
