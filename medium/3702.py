from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if set(nums) == {0}:
            return 0

        n = len(nums)
        cur = 0

        for num in nums:
            cur ^= num

        if cur == 0:
            return n - 1

        return n


def main():
    sol = Solution()
    print(sol.longestSubsequence([1,2,3]))
    print(sol.longestSubsequence([2,3,4]))

if __name__ == '__main__':
    main()