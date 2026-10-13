from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [abs(num) for num in nums]
        nums.sort()
        res = 0
        half = n // 2

        for i in range(n):
            if i < half:
                res -= nums[i] * nums[i]
            else:
                res += nums[i] * nums[i]

        return res

def main():
    sol = Solution()
    print(sol.maxAlternatingSum([1,2,3]))
    print(sol.maxAlternatingSum([1,-1,2,-2,3,-3]))

if __name__ == '__main__':
    main()