from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        res = temp = ListNode(-1, head)
        nums_set = set(nums)
        prev = None

        while temp:
            if temp.val in nums_set:
                if temp.next:
                    prev.next = temp.next
                else:
                    prev.next = None
            else:
                prev = temp

            temp = temp.next

        return res.next