from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(-1, n - 1):
            res = max(res, abs(nums[i] - nums[i + 1]))
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxAdjacentDistance([1,2,4]))
    print(sol.maxAdjacentDistance([-5,-10,-5]))

if __name__ == '__main__':
    main()