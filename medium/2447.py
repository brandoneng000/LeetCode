from typing import List
from math import gcd

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        for size in range(1, n + 1):
            for i in range(n - size + 1):
                if gcd(*nums[i: i + size]) == k:
                    res += 1
        
        return res
            
        
def main():
    sol = Solution()
    print(sol.subarrayGCD(nums = [9,3,1,2,6,3], k = 3))
    print(sol.subarrayGCD(nums = [4], k = 7))

if __name__ == '__main__':
    main()