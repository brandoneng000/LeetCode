from typing import List

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = -float('inf')

        for i in range(n - 1, -1, -1):
            if nums[i] > res:
                res = nums[i]
            else:
                res += nums[i]
        
        return res
        
def main():
    sol = Solution()
    print(sol.maxArrayValue([34,95,50,12,25,100,21,3,25,16,76,73,93,46,18]))
    print(sol.maxArrayValue([2,3,7,9,3]))
    print(sol.maxArrayValue([5,3,3]))

if __name__ == '__main__':
    main()