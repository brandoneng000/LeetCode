from typing import List
from heapq import heappush, heappop

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m, n = len(nums), len(nums[0])
        heaps = [[] for i in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                heappush(heaps[i], -nums[i][j])
        
        for j in range(n):
            cur = 0

            for i in range(m):
                cur = max(cur, -heappop(heaps[i]))
            
            res += cur
        
        return res

        
def main():
    sol = Solution()
    print(sol.matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))
    print(sol.matrixSum([[1]]))

if __name__ == '__main__':
    main()