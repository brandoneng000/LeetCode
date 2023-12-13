from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(num * num for index, num in enumerate(nums, 1) if len(nums) % index == 0)

    # def sumOfSquares(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     res = 0

    #     for index, num in enumerate(nums, 1):
    #         if n % index == 0:
    #             res += num * num
        
    #     return res

def main():
    sol = Solution()
    print(sol.sumOfSquares([1,2,3,4]))
    print(sol.sumOfSquares([2,7,1,19,18,3]))

if __name__ == '__main__':
    main()