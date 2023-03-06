from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_index, odd_index = 0, 1

        while even_index < len(nums) and odd_index < len(nums):
            if nums[even_index] % 2 == 0:
                even_index += 2
            elif nums[odd_index] % 2 == 1:
                odd_index += 2
            else:
                nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
                odd_index += 2
                even_index += 2
        
        return nums

def main():
    sol = Solution()
    print(sol.sortArrayByParityII([4,2,5,7]))
    print(sol.sortArrayByParityII([2,3]))

if __name__ == '__main__':
    main()