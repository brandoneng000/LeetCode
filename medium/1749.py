from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        small = 0
        large = 0
        cur = 0

        for n in nums:
            cur += n
            small = min(small, cur)
            large = max(large, cur)
        
        return large - small
        
def main():
    sol = Solution()
    print(sol.maxAbsoluteSum([1,-3,2,3,-4]))
    print(sol.maxAbsoluteSum([2,-5,1,-4,3,-2]))

if __name__ == '__main__':
    main()