from typing import List
from bisect import bisect_left

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        def longest_subseq(nums: List[int]):
            dp = [float('inf')] * (len(nums) + 1)

            for num in nums:
                dp[bisect_left(dp, num)] = num

            return dp.index(float('inf'))

        n = len(nums)
        max_found = 0

        for i in range(1, n - 1):
            left = [num for num in nums[:i] if num < nums[i]] + [nums[i]]
            right = [nums[i]] + [num for num in nums[i + 1:] if num < nums[i]]
            right = right[::-1]

            l, r = longest_subseq(left), longest_subseq(right)

            if l >= 2 and r >= 2:
                max_found = max(max_found, l + r - 1)
        
        return n - max_found
        
def main():
    sol = Solution()
    print(sol.minimumMountainRemovals([1,3,1]))
    print(sol.minimumMountainRemovals([2,1,1,5,6,2,3,1]))

if __name__ == '__main__':
    main()