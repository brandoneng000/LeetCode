from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, sum(nums)
        res = 0

        for i in range(n - 1):
            left += nums[i]
            right -= nums[i]
            res += left >= right
        
        return res
        
def main():
    sol = Solution()
    print(sol.waysToSplitArray([10,4,-8,7]))
    print(sol.waysToSplitArray([2,3,1,0]))

if __name__ == '__main__':
    main()