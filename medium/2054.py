from typing import List
from heapq import heappush, heappop

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        cur_max = 0
        res = 0

        for start, end, cur_val in events:
            heappush(heap, (end, cur_val))

            while heap and heap[0][0] < start:
                r, val = heappop(heap)
                cur_max = max(cur_max, val)

            res = max(res, cur_val + cur_max)
            
        return res

        
def main():
    sol = Solution()
    print(sol.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))
    print(sol.maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]))
    print(sol.maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]))

if __name__ == '__main__':
    main()