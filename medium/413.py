from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        arith = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                arith[i] = 1 + arith[i - 1]
        
        return sum(arith)


def main():
    sol = Solution()
    print(sol.numberOfArithmeticSlices([1,2,3,4]))
    print(sol.numberOfArithmeticSlices([1]))
    print(sol.numberOfArithmeticSlices([1,2,3,4,6,8,10]))
    print(sol.numberOfArithmeticSlices([1,2,3]))

if __name__ == '__main__':
    main()