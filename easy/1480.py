from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0

        for index in range(len(nums)):
            sum += nums[index]
            nums[index] = sum

        return nums

def main():
    sol = Solution()
    print(sol.runningSum([1,2,3,4]))
    print(sol.runningSum([1,1,1,1,1]))
    print(sol.runningSum([3,1,2,10,1]))

if __name__ == '__main__':
    main()