from typing import List
from math import lcm, gcd

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(-1, n):
            d, m = 0, 1

            for j in range(n):
                if j != i:
                    d = gcd(d, nums[j])
                    m = lcm(m, nums[j])
            
            res = max(res, d * m)

        return res
        
def main():
    sol = Solution()
    print(sol.maxScore([2,4,8,16]))
    print(sol.maxScore([1,2,3,4,5]))
    print(sol.maxScore([3]))

if __name__ == '__main__':
    main()