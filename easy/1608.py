from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        index = 0

        while index < len(nums) and nums[index] > index:
            index += 1
        
        return -1 if index < len(nums) and index == nums[index] else index

    
def main():
    sol = Solution()
    print(sol.specialArray([3,5]))
    print(sol.specialArray([0,0]))
    print(sol.specialArray([0,4,3,0,4]))
    print(sol.specialArray([6,6,6,6,6,6,6,6,6,6,6]))

if __name__ == '__main__':
    main()