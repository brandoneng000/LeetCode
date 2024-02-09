from typing import List
from heapq import heappush, heappop

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        largest_proj = max(milestones)

        if largest_proj > total // 2:
            return (total - largest_proj) * 2 + 1
        
        return total


    # def numberOfWeeks(self, milestones: List[int]) -> int:
    #     heap = []

    #     for i, milestone in enumerate(milestones):
    #         heappush(heap, (-milestone, i))
        
    #     res = 1
    #     hold_milestone, hold_index = heappop(heap)
    #     hold_milestone += 1

    #     while heap:
    #         next_milestone, next_index = heappop(heap)
    #         next_milestone += 1
    #         res += 1
            
    #         if hold_milestone < 0:
    #             heappush(heap, (hold_milestone, hold_index))
            
    #         hold_milestone, hold_index = next_milestone, next_index
        
    #     return res

        
def main():
    sol = Solution()
    print(sol.numberOfWeeks([1,2,3]))
    print(sol.numberOfWeeks([5,2,1]))

if __name__ == '__main__':
    main()