from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            positive = nums[i] > 0
            index = i
            cycle_size = 0
            while True:
                if (positive and nums[index] < 0) or (not positive and nums[index] > 0):
                    break
                next_index = (len(nums) + index + nums[index]) % len(nums)
                if next_index == index:
                    break
                index = next_index
                cycle_size += 1
                if cycle_size > len(nums):
                    return True

        return False


def main():
    sol = Solution()
    print(sol.circularArrayLoop([1,1,2]))
    print(sol.circularArrayLoop([2,-1,1,2,2]))
    print(sol.circularArrayLoop([-1,-2,-3,-4,-5,6]))
    print(sol.circularArrayLoop([1,-1,5,1,4]))
    print(sol.circularArrayLoop([-1,-2,-3,-4,-5]))

if __name__ == '__main__':
    main()