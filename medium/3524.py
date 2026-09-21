from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [0] * k
        dp = [0] * k

        for i in range(n):
            new_dp = [0] * k
            new_dp[nums[i] % k] += 1

            for r in range(k):
                new_dp[(r * nums[i]) % k] += dp[r]

            dp = new_dp

            for r in range(k):
                res[r] += dp[r]

        return res

def main():
    sol = Solution()
    print(sol.resultArray(nums = [1,2,3,4,5], k = 3))
    print(sol.resultArray(nums = [1,2,4,8,16,32], k = 4))

if __name__ == '__main__':
    main()