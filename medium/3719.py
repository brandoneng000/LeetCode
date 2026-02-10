from typing import List
from collections import Counter

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            odds = Counter()
            evens = Counter()

            for j in range(i, n):
                if nums[j] & 1:
                    odds[nums[j]] += 1
                else:
                    evens[nums[j]] += 1

                if len(odds) == len(evens):
                    res = max(res, j - i + 1)
        
        return res
        
def main():
    sol = Solution()
    print(sol.longestBalanced([2,5,4,3]))
    print(sol.longestBalanced([3,2,2,5,4]))
    print(sol.longestBalanced([1,2,3,2]))

if __name__ == '__main__':
    main()