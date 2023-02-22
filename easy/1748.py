from typing import List
import collections

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_count = collections.Counter(nums)
        result = 0

        for num in nums_count:
            if nums_count[num] == 1:
                result += num
        
        return result


def main():
    sol = Solution()
    print(sol.sumOfUnique([1,2,3,2]))
    print(sol.sumOfUnique([1,1,1,1,1]))
    print(sol.sumOfUnique([1,2,3,4,5]))

if __name__ == '__main__':
    main()