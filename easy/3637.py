from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        if nums[0] >= nums[1]:
            return False
        
        decreasing = False
        increasing = False

        for i in range(1, n - 1):
            if nums[i] == nums[i + 1]:
                return False
            
            if increasing and nums[i] > nums[i + 1]:
                return False

            if nums[i] > nums[i + 1] and not decreasing:
                decreasing = True

            if nums[i] < nums[i + 1] and not increasing and decreasing:
                increasing = True

        return decreasing and increasing
        
def main():
    sol = Solution()
    print(sol.isTrionic([1,3,5,4,2,6]))
    print(sol.isTrionic([2,1,3]))

if __name__ == '__main__':
    main()