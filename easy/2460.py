from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0

        return [n for n in nums if n] + [0] * nums.count(0)

def main():
    sol = Solution()
    print(sol.applyOperations([1,2,2,1,1,0]))
    print(sol.applyOperations([1,0,2,1,1,0]))
    print(sol.applyOperations([0,1]))

if __name__ == '__main__':
    main()