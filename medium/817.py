from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_dict = { n: None for n in nums }
        root = head

        while head:
            if head.val not in nums_dict:
                root = head
            else:
                nums_dict[head.val] = root
            head = head.next

        return len(set(nums_dict.values()))