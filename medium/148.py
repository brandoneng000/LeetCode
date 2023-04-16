from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def get_mid(head: ListNode):
            slow = ListNode(0, head)
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            mid = slow.next
            slow.next = None

            return mid
        
        def merge(list_node1: ListNode, list_node2: ListNode):
            temp_head = ListNode(-1000000)
            tail = temp_head

            while list_node1 and list_node2:
                if list_node1.val < list_node2.val:
                    tail.next = list_node1
                    list_node1 = list_node1.next
                    tail = tail.next
                else:
                    tail.next = list_node2
                    list_node2 = list_node2.next
                    tail = tail.next

            tail.next = list_node1 if list_node1 else list_node2
            return temp_head.next

        mid = get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)