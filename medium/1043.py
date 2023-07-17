from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            cur_max = 0
            for j in range(1, min(k, i) + 1):
                cur_max = max(cur_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + cur_max * j)
        
        return dp[n]


def main():
    sol = Solution()
    print(sol.maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))
    print(sol.maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4))
    print(sol.maxSumAfterPartitioning(arr = [1], k = 1))

if __name__ == '__main__':
    main()