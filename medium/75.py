from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED, WHITE = 0, 1
        red = 0
        white = 0
        blue = len(nums) - 1

        while white <= blue:
            if nums[white] == RED:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == WHITE:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


def main():
    sol = Solution()
    print(sol.sortColors([2,0,2,1,1,0]))
    print(sol.sortColors([2,0,1]))

if __name__ == '__main__':
    main()