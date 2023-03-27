from typing import List
import collections

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_count = collections.Counter(nums)
        return all(not nums_count[key] % 2 for key in nums_count)


def main():
    sol = Solution()
    print(sol.divideArray([3,2,3,2,2,2]))
    print(sol.divideArray([1,2,3,4]))

if __name__ == '__main__':
    main()