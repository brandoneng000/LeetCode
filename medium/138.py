from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # temp = new_head = Node(0)
        # origin = head

        # while origin:
        #     node = Node(origin.val)
        #     temp.next = node
        #     origin = origin.next
        #     temp = temp.next
        
        # temp = new_head.next
        # origin = head

        # while origin:
        #     if origin.random:
        #         temp_origin = head
        #         temp_temp = new_head.next
        #         while temp_origin != origin.random:
        #             temp_temp = temp_temp.next
        #             temp_origin = temp_origin.next
                
        #         temp.random = temp_temp
            
        #     origin = origin.next
        #     temp = temp.next

        # return new_head.next
        linked_list_dict = {}
        temp = new_head = Node(0)
        origin = head

        while origin:
            node = Node(origin.val)
            temp.next = node
            linked_list_dict[origin] = node
            origin = origin.next
            temp = temp.next

        temp = new_head.next
        origin = head

        while origin:
            if origin.random:
                temp.random = linked_list_dict[origin.random]
            temp = temp.next
            origin = origin.next
        
        return new_head.next


