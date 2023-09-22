from typing import List
import heapq
import collections

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = collections.deque()
        min_q = collections.deque()
        i = 0

        for num in nums:
            while max_q and num > max_q[-1]:
                max_q.pop()
            while min_q and num < min_q[-1]:
                min_q.pop()
            max_q.append(num)
            min_q.append(num)

            if max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[i]:
                    max_q.popleft()
                if min_q[0] == nums[i]:
                    min_q.popleft()
                i += 1
            
        return len(nums) - i

    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     min_heap = []
    #     max_heap = []
    #     i = 0
    #     res = 0

    #     for index, num in enumerate(nums):
    #         heapq.heappush(max_heap, (-num, index))
    #         heapq.heappush(min_heap, (num, index))
    #         while -max_heap[0][0] - min_heap[0][0] > limit:
    #             i = min(max_heap[0][1], min_heap[0][1]) + 1
    #             while max_heap[0][1] < i:
    #                 heapq.heappop(max_heap)
    #             while min_heap[0][1] < i:
    #                 heapq.heappop(min_heap)
    #         res = max(res, index - i + 1)
        
    #     return res

    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     n = len(nums)
    #     left = 0
    #     res = 1

    #     for right in range(n):
    #         while max(nums[left: right + 1]) - min(nums[left: right + 1]) > limit:
    #             left += 1
    #         res = max(res, right - left + 1)
        
    #     return res

def main():
    sol = Solution()
    print(sol.longestSubarray(nums = [8,2,4,7], limit = 4))
    print(sol.longestSubarray(nums = [10,1,2,4,7,2], limit = 5))
    print(sol.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0))

if __name__ == '__main__':
    main()