from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for n in nums:
            for i in dp[:]:
                dp[(n + i) % 3] = max(dp[(i + n) % 3], i + n)
        
        return dp[0]


    # def maxSumDivThree(self, nums: List[int]) -> int:
    #     def helper(total: int, index: int):
    #         if total % 3 == 0:
    #             self.res = max(self.res, total)
            
    #         for i in range(index, len(nums)):
    #             total += nums[i]
    #             helper(total, i + 1)
    #             total -= nums[i]

    #     self.res = 0
    #     helper(0, 0)
    #     return self.res

def main():
    sol = Solution()
    print(sol.maxSumDivThree([3,6,5,1,8]))
    print(sol.maxSumDivThree([4]))
    print(sol.maxSumDivThree([1,2,3,4,4]))

if __name__ == '__main__':
    main()