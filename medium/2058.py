from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        temp = head
        local_points = []
        index = 0
        min_dist = float('inf')

        while temp:
            if prev and temp.next:
                if prev.val < temp.val > temp.next.val or prev.val > temp.val < temp.next.val:
                    local_points.append(index)
            prev = temp
            temp = temp.next
            index += 1

        if len(local_points) <= 1:
            return [-1, -1]

        for i in range(len(local_points) - 1):
            min_dist = min(min_dist, local_points[i + 1] - local_points[i])
            
        return [min_dist, local_points[-1] - local_points[0]]
