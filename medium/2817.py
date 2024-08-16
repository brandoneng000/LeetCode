from typing import List
from heapq import heappush, heappop


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        sorted_nums = sorted([nums[i], i] for i in range(n))
        max_heap = []
        min_heap = []
        res = float('inf')

        for i in range(n):
            val, index = sorted_nums[i]
            heappush(min_heap, (index, val))
            heappush(max_heap, (-index, val))

            while min_heap and min_heap[0][0] + x <= index:
                res = min(res, val - heappop(min_heap)[1])
            
            while max_heap and max_heap[0][0] + x <= -index:
                res = min(res, val - heappop(max_heap)[1])
        
        return res

        
def main():
    sol = Solution()
    print(sol.minAbsoluteDifference(nums = [4,3,2,4], x = 2))
    print(sol.minAbsoluteDifference(nums = [5,3,2,10,15], x = 1))
    print(sol.minAbsoluteDifference(nums = [1,2,3,4], x = 3))

if __name__ == '__main__':
    main()