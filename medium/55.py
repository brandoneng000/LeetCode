from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        index = 0

        if len(nums) <= 1:
            return True

        while(jump > 0):
            jump -= 1
            index += 1

            if index == len(nums) - 1:
                return True
            
            if nums[index] > jump:
                jump = nums[index]

        return False
        
def main():
    sol = Solution()
    print(sol.canJump([2,3,1,1,4]))
    print(sol.canJump([3,2,1,0,4]))
    print(sol.canJump([0]))
    print(sol.canJump([2, 0, 0]))


if __name__ == '__main__':
    main()