from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        decrease = 1
        increase = 1

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                increase += 1
            else:
                increase = 1

            if nums[i] < nums[i + 1]:
                decrease += 1
            else:
                decrease = 1
            
            res = max(res, increase, decrease)
        
        return res
        
def main():
    sol = Solution()
    print(sol.longestMonotonicSubarray([1,4,3,3,2]))
    print(sol.longestMonotonicSubarray([3,3,3,3]))
    print(sol.longestMonotonicSubarray([3,2,1]))

if __name__ == '__main__':
    main()