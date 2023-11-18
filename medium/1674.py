from typing import List
from collections import Counter

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        difference = Counter()

        for i in range(n // 2):
            a, b = nums[i], nums[n - i - 1]

            difference[2] += 2
            difference[min(a, b) + 1] -= 1
            difference[a + b] -= 1
            difference[a + b + 1] += 1
            difference[max(a, b) + limit + 1] += 1
        
        cur = 0
        res = float('inf')

        for i in range(2, 2 * limit + 1):
            cur += difference[i]
            res = min(res, cur)
        
        return res


def main():
    sol = Solution()
    print(sol.minMoves(nums = [1,2,4,3], limit = 4))
    print(sol.minMoves(nums = [1,2,2,1], limit = 2))
    print(sol.minMoves(nums = [1,2,1,2], limit = 2))

if __name__ == '__main__':
    main()