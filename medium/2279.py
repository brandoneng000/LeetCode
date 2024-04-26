from typing import List
from heapq import heappush, heappop

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        heap = []
        res = 0

        for i in range(n):
            cap = capacity[i] - rocks[i]
            
            if cap == 0:
                res += 1
            else:
                heappush(heap, cap)
        
        while heap and additionalRocks:
            cur = heappop(heap)
            
            if cur <= additionalRocks:
                additionalRocks -= cur
                res += 1
            else:
                break
        
        return res
        
def main():
    sol = Solution()
    print(sol.maximumBags(capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2))
    print(sol.maximumBags(capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100))

if __name__ == '__main__':
    main()