from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0

        for index in range(len(nums) - 1):
            if nums[index] >= nums[index + 1]:
                result += nums[index] - nums[index + 1] + 1
                nums[index + 1] = nums[index] + 1
        
        return result


def main():
    sol = Solution()
    print(sol.minOperations([1,1,1]))
    print(sol.minOperations([1,5,2,4,1]))
    print(sol.minOperations([8]))

if __name__ == '__main__':
    main()