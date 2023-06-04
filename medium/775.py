from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        global_inversions = local_inversions = 0

        for index, num in enumerate(nums):
            if num > index:
                global_inversions += num - index
            elif num < index:
                global_inversions += index - num - 1
            
            if index < len(nums) - 1 and num > nums[index + 1]:
                local_inversions += 1
        
        return global_inversions == local_inversions


def main():
    sol = Solution()
    print(sol.isIdealPermutation([1,0,2]))
    print(sol.isIdealPermutation([1,2,0]))

if __name__ == '__main__':
    main()