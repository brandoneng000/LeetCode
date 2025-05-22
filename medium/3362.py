from typing import List
from heapq import heappush, heappop

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        queries.sort()
        delta = [0] * (n + 1)
        operations = 0
        heap = []
        j = 0

        for i in range(n):
            operations += delta[i]

            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            
            while operations < nums[i] and heap and -heap[0] >= i:
                operations += 1
                delta[-heappop(heap) + 1] -= 1
            
            if operations < nums[i]:
                return -1
        
        return len(heap)


def main():
    sol = Solution()
    print(sol.maxRemoval(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]))
    print(sol.maxRemoval(nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]))
    print(sol.maxRemoval(nums = [1,2,3,4], queries = [[0,3]]))

if __name__ == '__main__':
    main()