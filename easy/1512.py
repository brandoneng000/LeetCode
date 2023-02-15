from typing import List
import collections

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_dict = collections.Counter(nums)
        result = 0

        for num in nums_dict:
            if nums_dict[num] > 1:
                result += nums_dict[num] * (nums_dict[num] - 1) // 2
        
        return result


def main():
    sol = Solution()
    print(sol.numIdenticalPairs([1,2,3,1,1,3]))
    print(sol.numIdenticalPairs([1,1,1,1]))
    print(sol.numIdenticalPairs([1,2,3]))

if __name__ == '__main__':
    main()