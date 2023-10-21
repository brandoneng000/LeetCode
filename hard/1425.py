from typing import List
import heapq
import collections

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = collections.deque()
        dp = [0] * n

        for i in range(n):
            if q and i - q[0] > k:
                q.popleft()
            
            dp[i] = (dp[q[0]] if q else 0) + nums[i]

            while q and dp[q[-1]] < dp[i]:
                q.pop()
            
            if dp[i] > 0:
                q.append(i)
        
        return max(dp)

    # def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     heap = [(-nums[0], 0)]
    #     res = nums[0]

    #     for i in range(1, n):
    #         while i - heap[0][1] > k:
    #             heapq.heappop(heap)
            
    #         cur = max(0, -heap[0][0]) + nums[i]
    #         res = max(res, cur)
    #         heapq.heappush(heap, (-cur, i))
        
    #     return res


    # def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    #     def add_next(cur_sum: int, index: int):
    #         self.res = max(self.res, cur_sum)

    #         for i in range(index, min(index + k, n)):
    #             add_next(cur_sum + nums[i], i + 1)

    #     n = len(nums)
    #     self.res = -float('inf')

    #     for i in range(n):
    #         add_next(nums[i], i + 1)
        
    #     return self.res
        
def main():
    sol = Solution()
    print(sol.constrainedSubsetSum(nums = [10,2,-10,5,20], k = 2))
    print(sol.constrainedSubsetSum(nums = [-1,-2,-3], k = 1))
    print(sol.constrainedSubsetSum(nums = [10,-2,-10,-5,20], k = 2))

if __name__ == '__main__':
    main()