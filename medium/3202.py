from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0 for j in range(k)] for i in range(k)]
        res = 1

        for num in nums:
            cur = num % k

            for i in range(k):
                prev = (i - cur + k) % k
                dp[cur][i] = max(dp[cur][i], dp[prev][i] + 1)
                res = max(res, dp[cur][i])
        
        return res
        
def main():
    sol = Solution()
    print(sol.maximumLength(nums = [1,2,3,4,5], k = 2))
    print(sol.maximumLength(nums = [1,4,2,3,1,4], k = 3))

if __name__ == '__main__':
    main()