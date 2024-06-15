from typing import List
from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        gain = sorted(zip(profits, capital), key=lambda x: x[1])
        heap = []
        i = 0

        for _ in range(k):
            while i < n and gain[i][1] <= w:
                heappush(heap, -gain[i][0])
                i += 1
            
            if heap:
                w -= heappop(heap)
        
        return w

    # def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    #     gains = sorted([[p, c] for p, c in zip(profits, capital)], reverse=True)
    #     visited = set()
    #     res = w

    #     for _ in range(k):
    #         for i, (p, c) in enumerate(gains):
    #             if c <= w and i not in visited:
    #                 visited.add(i)
    #                 res += p
    #                 w += p
    #                 break
        
    #     return res
        
def main():
    sol = Solution()
    print(sol.findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))
    print(sol.findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))

if __name__ == '__main__':
    main()