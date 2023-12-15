from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n1, n2, temp = None, None, head

        while temp:
            k -= 1
            n2 = None if not n2 else n2.next
            
            if k == 0:
                n1 = temp
                n2 = head
            temp = temp.next
        
        n1.val, n2.val = n2.val, n1.val

        return head

    # def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     def get_size(head: ListNode) -> int:
    #         temp = head
    #         n = 0

    #         while temp:
    #             temp = temp.next
    #             n += 1
            
    #         return n
        
    #     n = get_size(head)
    #     if n == 1:
    #         return head
        
    #     swap = n - k
    #     begin = head
    #     begin_prev = None
    #     end = head
    #     end_prev = None
    #     count = 1

    #     while count != k:
    #         begin_prev = begin
    #         begin = begin.next
    #         count += 1
        
    #     count = 0
    #     while count != swap:
    #         end_prev = end
    #         end = end.next
    #         count += 1

    #     if not begin_prev:
    #         end_prev.next = head
    #         head.next, end.next = None, head.next
    #         return end
    #     elif not end_prev:
    #         return self.swapNodes(head, 1)
    #     else:
    #         end_prev.next, begin_prev.next = begin, end
    #         end.next, begin.next = begin.next, end.next

    #     return head