from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        left = 0

        for right in range(1, n - 1):
            if nums[right] != nums[right + 1]:
                if (
                    (nums[right] > nums[left] and nums[right] > nums[right + 1])
                    or (nums[right] < nums[left] and nums[right] < nums[right + 1])
                ):
                    res += 1
                left = right
            
        return res

    # def countHillValley(self, nums: List[int]) -> int:
    #     res = 0
    #     up = False
    #     down = False

    #     for i in range(len(nums) - 1):
    #         if nums[i] == nums[i + 1]:
    #             pass
    #         elif nums[i] < nums[i + 1]:
    #             up = True
    #             if down:
    #                 res += 1
    #             down = False
    #         elif nums[i] > nums[i + 1]:
    #             down = True
    #             if up:
    #                 res += 1
    #             up = False
        
    #     return res

def main():
    sol = Solution()
    print(sol.countHillValley([2,4,1,1,6,5]))
    print(sol.countHillValley([6,6,5,5,4,1]))
    print(sol.countHillValley([1,1,1,1,1,1,1,57,57,57,50,50,50,50,22,22,22,86]))

if __name__ == '__main__':
    main()