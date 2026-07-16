from typing import List
from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        m = 0
        prefix_gcd = []
        res = 0

        for i in range(n):
            m = max(m, nums[i])
            prefix_gcd.append(gcd(nums[i], m))
        
        prefix_gcd.sort()
        left = 0
        right = n - 1

        while left < right:
            res += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.gcdSum([2,6,4]))
    print(sol.gcdSum([3,6,2,8]))

if __name__ == '__main__':
    main()