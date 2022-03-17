# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        size = 0
        temp = head

        while temp:
            size += 1
            temp = temp.next

        if size == 1:
            return []

        temp = head
        prev = ListNode(0, head)
        store = prev

        while temp:
            if counter == size - n:
                prev.next = temp.next
                break
            else:
                counter += 1
                prev = temp
                temp = temp.next

        return store.next

