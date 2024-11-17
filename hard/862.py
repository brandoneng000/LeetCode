from typing import List
from heapq import heappop, heappush
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        res = float('inf')
        cur_sum = 0

        for r in range(n):
            cur_sum += nums[r]

            if cur_sum >= k:
                res = min(res, r + 1)

            while q and cur_sum - q[0][0] >= k:
                prefix, end_index = q.popleft()
                res = min(res, r - end_index)
            
            while q and q[-1][0] >= cur_sum:
                q.pop()

            q.append((cur_sum, r))

        return res if res != float('inf') else -1


    # def shortestSubarray(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     res = float('inf')
    #     cur_sum = 0
    #     heap = []

    #     for r in range(n):
    #         cur_sum += nums[r]

    #         if cur_sum >= k:
    #             res = min(res, r + 1)

    #         while heap and cur_sum - heap[0][0] >= k:
    #             prefix, end_index = heappop(heap)
    #             res = min(res, r - end_index)

    #         heappush(heap, (cur_sum, r))

    #     return res if res != float('inf') else -1

    # def shortestSubarray(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     res = float('inf')

    #     for i in range(n):
    #         cur = 0
    #         for j in range(i, min(i + res + 1, n)):
    #             cur += nums[j]

    #             if cur >= k:
    #                 res = min(res, j - i + 1)
    #                 break
        
    #     return res if res != float('inf') else -1
        

def main():
    sol = Solution()
    print(sol.shortestSubarray(nums = [-28,81,-20,28,-29], k = 89))
    print(sol.shortestSubarray(nums = [1], k = 1))
    print(sol.shortestSubarray(nums = [1,2], k = 4))
    print(sol.shortestSubarray(nums = [2,-1,2], k = 3))

if __name__ == '__main__':
    main()