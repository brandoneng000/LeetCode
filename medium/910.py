from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        small, large = nums[0], nums[-1]
        res = large - small

        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1]
            res = min(res, max(large - k, a + k) - min(small + k, b - k))
        
        return res

def main():
    sol = Solution()
    print(sol.smallestRangeII(nums = [1], k = 0))
    print(sol.smallestRangeII(nums = [0,10], k = 2))
    print(sol.smallestRangeII(nums = [1,3,6], k = 3))
    print(sol.smallestRangeII(nums = [1,3,6,8], k = 3))

if __name__ == '__main__':
    main()