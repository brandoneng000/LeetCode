from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        large_j = nums[-1]
        result = -1

        for index in range(len(nums) - 2, -1, -1):
            result = max(result, large_j - nums[index])
            large_j = max(nums[index], large_j)
            
        return result if result != 0 else -1


def main():
    sol = Solution()
    print(sol.maximumDifference([7,1,5,4]))
    print(sol.maximumDifference([9,4,3,2]))
    print(sol.maximumDifference([1,5,2,10]))

if __name__ == '__main__':
    main()