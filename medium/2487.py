from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_linked_list(head: ListNode):
            prev = None

            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            
            return prev
        
        head = reverse_linked_list(head)
        temp = res = head

        while temp.next:
            if temp.next.val < temp.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return reverse_linked_list(res)
    
    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     def reverse_linked_list(head: ListNode):
    #         prev = None

    #         while head:
    #             next = head.next
    #             head.next = prev
    #             prev = head
    #             head = next
            
    #         return prev
        
    #     head = reverse_linked_list(head)
    #     temp = res = head

    #     while temp:
    #         next = temp.next

    #         while next and next.val < temp.val:
    #             next = next.next
            
    #         temp.next = next
    #         temp = temp.next
        
    #     return reverse_linked_list(res)


    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     stack = []
    #     res = ListNode()
        
    #     while head:
    #         while stack and stack[-1] < head.val:
    #             stack.pop()
    #         stack.append(head.val)
    #         head = head.next
        
    #     temp = res
    #     for num in stack:
    #         temp.next = ListNode(num)
    #         temp = temp.next
        
    #     return res.next