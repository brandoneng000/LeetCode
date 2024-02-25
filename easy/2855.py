from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                nums = nums[i:] + nums[:i]
                return n - i if sorted(nums) == nums else -1
        
        return 0
        
        
def main():
    sol = Solution()
    print(sol.minimumRightShifts([3,4,5,1,2]))
    print(sol.minimumRightShifts([1,3,5]))
    print(sol.minimumRightShifts([2,1,4]))

if __name__ == '__main__':
    main()