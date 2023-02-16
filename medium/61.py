from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        
        temp = head
        count = 1

        while temp.next:
            temp = temp.next
            count += 1


        k = k % count
        temp.next = head
        temp = head

        print(temp.val)

        for _ in range(count - k - 1):
            temp = temp.next
        
        head = temp.next
        temp.next = None

        return head

