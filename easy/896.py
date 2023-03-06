from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mono_increase = True
        mono_decrease = True

        for index in range(len(nums) - 1):
            if nums[index] < nums[index + 1]:
                mono_decrease = False
            elif nums[index] > nums[index + 1]:
                mono_increase = False
        
        return mono_increase or mono_decrease
    
def main():
    sol = Solution()
    print(sol.isMonotonic([1,2,2,3]))
    print(sol.isMonotonic([6,5,4,4]))
    print(sol.isMonotonic([1,3,2]))

if __name__ == '__main__':
    main()