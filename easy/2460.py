from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero = 0

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            zero += 1 if nums[i] == 0 else 0

        zero += 1 if nums[-1] == 0 else 0
        return [num for num in nums if num] + [0] * zero

    # def applyOperations(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     zero = 0
    #     res = []

    #     for i in range(n):
    #         if i + 1 < n and nums[i] == nums[i + 1]:
    #             nums[i] *= 2
    #             nums[i + 1] = 0
    #         if nums[i] == 0:
    #             zero += 1
    #         else:
    #             res.append(nums[i])

    #     return res + [0] * zero


    # def applyOperations(self, nums: List[int]) -> List[int]:
    #     for index in range(len(nums) - 1):
    #         if nums[index] == nums[index + 1]:
    #             nums[index] *= 2
    #             nums[index + 1] = 0

    #     return [n for n in nums if n] + [0] * nums.count(0)

def main():
    sol = Solution()
    print(sol.applyOperations([1,2,2,1,1,0]))
    print(sol.applyOperations([1,0,2,1,1,0]))
    print(sol.applyOperations([0,1]))

if __name__ == '__main__':
    main()