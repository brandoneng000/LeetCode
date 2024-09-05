from typing import List

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = { target: 0 }

        for num in nums:
            temp = dp.copy()

            for cur in list(dp.keys()):
                if cur - num < 0:
                    continue
                else:
                    dp[cur - num] = max(dp.get(cur - num, -1), temp[cur] + 1)
        
        return dp.get(0, -1)

        
def main():
    sol = Solution()
    print(sol.lengthOfLongestSubsequence(nums = [2,1,8,4,7,2,10,1], target = 22))
    print(sol.lengthOfLongestSubsequence(nums = [1,2,3,4,5], target = 9))
    print(sol.lengthOfLongestSubsequence(nums = [4,1,3,2,1,5], target = 7))
    print(sol.lengthOfLongestSubsequence(nums = [1,1,5,4,5], target = 3))

if __name__ == '__main__':
    main()