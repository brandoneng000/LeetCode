from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        array = []
        temp = head
        
        while temp:
            array.append(temp)
            temp = temp.next
        
        alternate = True
        head = temp = array.pop(0)
        while array:
            if alternate:
                node = array.pop()
            else:
                node = array.pop(0)
            temp.next = node
            temp = temp.next
            alternate = not alternate
        
        return head