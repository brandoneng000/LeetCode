from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        initial = 0

        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                initial = index + 1
                break

        size = len(nums)
        nums += nums

        nums = nums[initial: initial + size]
        return sorted(nums) == nums


def main():
    sol = Solution()
    print(sol.check([3,4,5,1,2]))
    print(sol.check([2,1,3,4]))
    print(sol.check([1,2,3]))
    print(sol.check([6,10,6]))

if __name__ == '__main__':
    main()