from typing import Optional
import random
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        temp = head
        self.length = 0
        while temp:
            temp = temp.next
            self.length += 1

    def getRandom(self) -> int:
        count = random.randint(0, self.length - 1)
        temp = self.head
        while count:
            temp = temp.next
            count -= 1
        
        return temp.val
