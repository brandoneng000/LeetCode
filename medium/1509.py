from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        res = float('inf')

        for a, b in zip(nums[:4], nums[-4:]):
            res = min(res, b - a)
        
        return res

    # def minDifference(self, nums: List[int]) -> int:
    #     if len(nums) <= 4:
    #         return 0
        
    #     n = len(nums)
    #     nums.sort()
    #     res = float('inf')

    #     for i in range(0, 4):
    #         res = min(res, nums[n - (3 - i) - 1] - nums[i])
        
    #     return res
        

def main():
    sol = Solution()
    print(sol.minDifference([6,6,0,1,1,4,6]))
    print(sol.minDifference([5,3,2,4]))
    print(sol.minDifference([1,5,0,10,14]))
    print(sol.minDifference([3,100,20]))

if __name__ == '__main__':
    main()