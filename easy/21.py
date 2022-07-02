from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # temp = head = ListNode()

        # while list1 or list2:
        #     if not list1:
        #         temp.next = list2
        #         list2 = list2.next
        #     elif not list2:
        #         temp.next = list1
        #         list1 = list1.next
        #     else:
        #         if list1.val <= list2.val:
        #             temp.next = list1
        #             list1 = list1.next
        #         else:
        #             temp.next = list2
        #             list2 = list2.next
            
        #     temp = temp.next
        
        # return head.next
        temp = head = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 if list1 else list2
        return head.next