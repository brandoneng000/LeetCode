from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count = 0
        prev = nums[0]

        for index in range(1, len(nums)):
            if prev < nums[index]:
                prev = nums[index]
            else:
                count += 1
                if index >= 2:
                    if nums[index] > nums[index - 2]:
                        prev = min(prev, nums[index])
                else:
                    prev = nums[index]
        
        return count < 2
            

def main():
    sol = Solution()
    print(sol.canBeIncreasing([1,2,10,5,7]))
    print(sol.canBeIncreasing([2,3,1,2]))
    print(sol.canBeIncreasing([1,1,1]))
    print(sol.canBeIncreasing([100, 21, 100]))

if __name__ == '__main__':
    main()