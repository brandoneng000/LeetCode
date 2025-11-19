from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        
        return original

    # def findFinalValue(self, nums: List[int], original: int) -> int:
    #     times_two = {}

    #     for num in nums:
    #         times_two[num] = num * 2

    #     while original in times_two:
    #         original = times_two[original]
        
    #     return original

    # def findFinalValue(self, nums: List[int], original: int) -> int:
    #     nums = set(nums)

    #     while original in nums:
    #         original *= 2
        
    #     return original

def main():
    sol = Solution()
    print(sol.findFinalValue(nums = [5,3,6,1,12], original = 3))
    print(sol.findFinalValue(nums = [2,7,9], original = 4))

if __name__ == '__main__':
    main()