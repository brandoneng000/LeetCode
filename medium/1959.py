from typing import List

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cache = {}

        def dp(index: int, k: int):
            if index == n:
                return 0
            if k < 0:
                return float('inf')
            
            if (index, k) in cache:
                return cache[(index, k)]

            res = float('inf')
            cur_sum = 0
            cur_max = 0

            for i in range(index, n):
                cur_max = max(cur_max, nums[i])
                cur_sum += nums[i]
                res = min(res, cur_max * (i - index + 1) - cur_sum + dp(i + 1, k - 1))
            
            cache[(index, k)] = res
            return res
        
        return dp(0, k)

        
def main():
    sol = Solution()
    print(sol.minSpaceWastedKResizing(nums = [10,20], k = 0))
    print(sol.minSpaceWastedKResizing(nums = [10,20,30], k = 1))
    print(sol.minSpaceWastedKResizing(nums = [10,20,15,30,20], k = 2))

if __name__ == '__main__':
    main()