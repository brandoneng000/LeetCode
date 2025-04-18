from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"

        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"
        return "scalene"
        
def main():
    sol = Solution()
    print(sol.triangleType([8,4,2]))
    print(sol.triangleType([3,3,3]))
    print(sol.triangleType([3,4,5]))

if __name__ == '__main__':
    main()