from typing import List
import heapq

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        def average(i, j):
            return (prefix[j] - prefix[i]) / (j - i)

        size = len(nums)
        dp = [average(i, size) for i in range(size)]
        for k in range(k - 1):
            for i in range(size):
                for j in range(i + 1, size):
                    dp[i] = max(dp[i], average(i, j) + dp[j])
        
        return dp[0]
        


def main():
    sol = Solution()
    print(sol.largestSumOfAverages(nums = [9,1,2,3,9], k = 3))
    print(sol.largestSumOfAverages(nums = [1,2,3,4,5,6,7], k = 4))

if __name__ == '__main__':
    main()