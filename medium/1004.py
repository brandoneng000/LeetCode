from typing import List
import collections

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero = 0
        res = 0

        for right, bit in enumerate(nums):
            if bit == 0:
                zero += 1
            
            if zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            
            if zero <= k:
                res = max(res, right - left + 1)
        
        return res
        

def main():
    sol = Solution()
    print(sol.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
    print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))

if __name__ == '__main__':
    main()