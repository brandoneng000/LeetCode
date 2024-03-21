from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        temp = head
        nums = []

        while temp:
            n += 1
            nums.append(temp.val)
            temp = temp.next
        
        return max(nums[i] + nums[n - 1 - i] for i in range(n // 2))
