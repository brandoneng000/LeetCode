from typing import List
from collections import Counter
from bisect import bisect_left

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        sum_count = Counter()
        min_arr = []
        max_arr = []

        for i in range(n // 2):
            a = min(nums[i], nums[n - i - 1])
            b = max(nums[i], nums[n - i - 1])

            sum_count[a + b] += 1
            min_arr.append(a)
            max_arr.append(b)

        min_arr.sort()
        max_arr.sort()
        
        res = n
        
        for c in range(2, 2 * limit + 1):
            left = n // 2 - bisect_left(min_arr, c)
            right = bisect_left(max_arr, c - limit)

            cur = n // 2 + left + right - sum_count[c]
            res = min(res, cur)
        
        return res

    # def minMoves(self, nums: List[int], limit: int) -> int:
    #     n = len(nums)
    #     difference = Counter()

    #     for i in range(n // 2):
    #         a, b = nums[i], nums[n - i - 1]

    #         difference[2] += 2
    #         difference[min(a, b) + 1] -= 1
    #         difference[a + b] -= 1
    #         difference[a + b + 1] += 1
    #         difference[max(a, b) + limit + 1] += 1
        
    #     cur = 0
    #     res = float('inf')

    #     for i in range(2, 2 * limit + 1):
    #         cur += difference[i]
    #         res = min(res, cur)
        
    #     return res


def main():
    sol = Solution()
    print(sol.minMoves(nums = [1,2,4,3], limit = 4))
    print(sol.minMoves(nums = [1,2,2,1], limit = 2))
    print(sol.minMoves(nums = [1,2,1,2], limit = 2))

if __name__ == '__main__':
    main()