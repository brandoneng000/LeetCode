from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_node = None
        prev_index = -1
        first_index = -1
        temp = head
        min_dist = float('inf')
        index = 0

        while temp:
            if prev_node and temp.next:
                if prev_node.val < temp.val > temp.next.val or prev_node.val > temp.val < temp.next.val:
                    if first_index == -1:
                        first_index = index
                    if prev_index != -1:
                        min_dist = min(min_dist, index - prev_index)
                    prev_index = index
            prev_node = temp
            temp = temp.next
            index += 1

        if first_index == prev_index:
            return [-1, -1]
        return [min_dist, prev_index - first_index]


    # def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    #     prev = None
    #     temp = head
    #     local_points = []
    #     index = 0
    #     min_dist = float('inf')

    #     while temp:
    #         if prev and temp.next:
    #             if prev.val < temp.val > temp.next.val or prev.val > temp.val < temp.next.val:
    #                 local_points.append(index)
    #         prev = temp
    #         temp = temp.next
    #         index += 1

    #     if len(local_points) <= 1:
    #         return [-1, -1]

    #     for i in range(len(local_points) - 1):
    #         min_dist = min(min_dist, local_points[i + 1] - local_points[i])
            
    #     return [min_dist, local_points[-1] - local_points[0]]
