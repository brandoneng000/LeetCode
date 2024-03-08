from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        max_count = max(nums_count.values())
        res = 0

        for num in nums_count:
            if nums_count[num] == max_count:
                res += nums_count[num]

        return res
        
def main():
    sol = Solution()
    print(sol.maxFrequencyElements([1,2,2,3,1,4]))
    print(sol.maxFrequencyElements([1,2,3,4,5]))

if __name__ == '__main__':
    main()