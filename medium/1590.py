from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = sum(nums) 
        target = total % p

        if target == 0:
            return 0
        
        dp = { 0: -1 }
        cur_sum = 0
        res = n

        for i in range(n):
            cur_sum = (cur_sum + nums[i]) % p
            needed = (cur_sum - target + p) % p

            if needed in dp:
                res = min(res, i - dp[needed])
            
            dp[cur_sum] = i
        
        return -1 if res == n else res
        

    # def minSubarray(self, nums: List[int], p: int) -> int:
    #     n = len(nums)
    #     remove_remainder = sum(nums) % p
    #     dp = { 0: -1 }
    #     cur = 0
    #     res = n

    #     for i, num in enumerate(nums):
    #         cur = (cur + num) % p
    #         dp[cur] = i

    #         if (cur - remove_remainder) % p in dp:
    #             res = min(res, i - dp[(cur - remove_remainder) % p])
        
    #     return res if res < n else -1
        
def main():
    sol = Solution()
    print(sol.minSubarray(nums = [3,1,4,2], p = 6))
    print(sol.minSubarray(nums = [6,3,5,2], p = 9))
    print(sol.minSubarray(nums = [1,2,3], p = 3))

if __name__ == '__main__':
    main()