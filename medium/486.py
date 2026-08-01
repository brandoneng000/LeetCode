from typing import List
import collections

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(l, r):
            if dp[l][r] != -1:
                return dp[l][r]
            if l == r:
                return nums[l]

            left = nums[l] - helper(l + 1, r)
            right = nums[r] - helper(l, r - 1)
            dp[l][r] = max(left, right)

            return dp[l][r]

        n = len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return helper(0, n - 1) >= 0

    # def PredictTheWinner(self, nums: List[int]) -> bool:
    #     dp = collections.defaultdict(int)

    #     def helper(left, right):
    #         if left == right:
    #             return nums[left]
    #         if (left, right) in dp:
    #             return dp[(left, right)]
            
    #         score_left = nums[left] - helper(left + 1, right)
    #         score_right = nums[right] - helper(left, right - 1)
    #         dp[(left, right)] = max(score_left, score_right)

    #         return dp[(left, right)]
        
    #     return helper(0, len(nums) - 1) >= 0

    # def PredictTheWinner(self, nums: List[int]) -> bool:
    #     def helper(left, right):
    #         if left == right:
    #             return nums[left]
            
    #         score_left = nums[left] - helper(left + 1, right)
    #         score_right = nums[right] - helper(left, right - 1)

    #         return max(score_left, score_right)

    #     return helper(0, len(nums) - 1) >= 0

def main():
    sol = Solution()
    print(sol.PredictTheWinner([1,5,2]))
    print(sol.PredictTheWinner([1,5,233,7]))

if __name__ == '__main__':
    main()