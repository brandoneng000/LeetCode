from typing import List
import collections

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums_count = collections.Counter(nums)
        res = 0
        taken = []

        for i in range(len(nums) + max(nums)):
            if nums_count[i] > 1:
                taken.extend([i] * (nums_count[i] - 1))
            elif taken and nums_count[i] == 0:
                res += i - taken.pop()
        
        return res


def main():
    sol = Solution()
    print(sol.minIncrementForUnique([1,5,5,5]))
    print(sol.minIncrementForUnique([1,2,2]))
    print(sol.minIncrementForUnique([3,2,1,2,1,7]))

if __name__ == '__main__':
    main()