from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res, dp = 0, 0
        prev = -1

        for i in range(len(nums)):
            if nums[i] < left and i > 0:
                res += dp
            if nums[i] > right:
                dp = 0
                prev = i
            if left <= nums[i] <= right:
                dp = i - prev
                res += dp

        return res


def main():
    sol = Solution()
    # print(sol.numSubarrayBoundedMax(nums = [73,55,36,5,55,14,9,7,72,52], left = 32, right = 69))
    print(sol.numSubarrayBoundedMax(nums = [2,1,4,3], left = 2, right = 3))
    print(sol.numSubarrayBoundedMax(nums = [2,9,2,5,6], left = 2, right = 8))

if __name__ == '__main__':
    main()