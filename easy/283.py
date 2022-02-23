from typing import List

class Solution(object):
    def moveZeroes(self, nums: List[int]) -> None:
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0
        size = len(nums)
        while index < size:
            check = nums[index]
            if check == 0:
                size -= 1
                nums.pop(index)
                nums.append(0)
            else:
                index += 1

        return nums
        
def main():
    sol = Solution()
    print(sol.moveZeroes([0,1,0,3,12]))
    print(sol.moveZeroes([0]))
    print(sol.moveZeroes([0,0,0,0,1]))

if __name__ == '__main__':
    main()