from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        heap = []
        res = day = 0
        
        while events or heap:
            if not heap:
                day = events[-1][0]
            
            while events and events[-1][0] <= day:
                heapq.heappush(heap, events.pop()[1])
            
            heapq.heappop(heap)
            res += 1
            day += 1
            
            while heap and heap[0] < day:
                heapq.heappop(heap)
        
        return res


def main():
    sol = Solution()
    print(sol.maxEvents([[1,2],[2,3],[3,4]]))
    print(sol.maxEvents([[1,2],[2,3],[3,4],[1,2]]))

if __name__ == '__main__':
    main()