from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        remove_remainder = sum(nums) % p
        dp = { 0: -1 }
        cur = 0
        res = n

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            dp[cur] = i

            if (cur - remove_remainder) % p in dp:
                res = min(res, i - dp[(cur - remove_remainder) % p])
        
        return res if res < n else -1
        
def main():
    sol = Solution()
    print(sol.minSubarray(nums = [3,1,4,2], p = 6))
    print(sol.minSubarray(nums = [6,3,5,2], p = 9))
    print(sol.minSubarray(nums = [1,2,3], p = 3))

if __name__ == '__main__':
    main()