from typing import List
from math import lcm, gcd

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            prod_total = nums[i]
            lcm_total = nums[i]
            gcd_total = nums[i]

            for j in range(i + 1, n):
                prod_total *= nums[j]
                lcm_total = lcm(lcm_total, nums[j])
                gcd_total = gcd(gcd_total, nums[j])

                if prod_total > gcd_total * lcm_total:
                    break
                elif prod_total == gcd_total * lcm_total:
                    res = max(res, j - i + 1)

        return res
        

def main():
    sol = Solution()
    print(sol.maxLength([1,2,1,2,1,1,1]))
    print(sol.maxLength([2,3,4,5,6]))
    print(sol.maxLength([1,2,3,1,4,5,1]))

if __name__ == '__main__':
    main()