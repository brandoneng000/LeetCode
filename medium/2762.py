from typing import List
from heapq import heappush, heappop

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        max_heap = []
        min_heap = []
        res = left = 0

        for r in range(n):
            heappush(max_heap, (-nums[r], r))
            heappush(min_heap, (nums[r], r))

            while abs(-max_heap[0][0] - min_heap[0][0]) > 2:
                if max_heap[0][1] > min_heap[0][1]:
                    left = max(left, heappop(min_heap)[1] + 1)
                else:
                    left = max(left, heappop(max_heap)[1] + 1)
                
                while max_heap and left > max_heap[0][1]:
                    heappop(max_heap)
                
                while min_heap and left > min_heap[0][1]:
                    heappop(min_heap)
                
            res += r - left + 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.continuousSubarrays([5,4,2,4]))
    print(sol.continuousSubarrays([1,2,3]))

if __name__ == '__main__':
    main()