from typing import List

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        prefix_negative = sorted([num for num in nums if num < 0])
        prefix_positive = [num for num in nums if num > 0]
        zero = nums.count(0)

        for i in range(1, len(prefix_negative)):
            prefix_negative[i] *= prefix_negative[i - 1]
        
        for i in range(1, len(prefix_positive)):
            prefix_positive[i] *= prefix_positive[i - 1]

        largest_negative = max(prefix_negative) if prefix_negative else 1

        if not prefix_negative and not prefix_positive:
            return 0
        elif largest_negative < 0 and zero:
            return prefix_positive[-1] if prefix_positive else 0
        elif largest_negative < 0 and not prefix_positive:
            return max(nums)
        elif largest_negative < 0 and prefix_positive:
            return prefix_positive[-1]
        
        return largest_negative * (prefix_positive[-1] if prefix_positive else 1)
        
def main():
    sol = Solution()
    print(sol.maxStrength([0, -1]))
    print(sol.maxStrength([3,-1,-5,2,5,-9]))
    print(sol.maxStrength([-4,-5,-4]))

if __name__ == '__main__':
    main()