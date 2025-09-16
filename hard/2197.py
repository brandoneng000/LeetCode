from typing import List
from math import lcm, gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            while res and gcd(res[-1], num) > 1:
                num = lcm(res.pop(), num)
            
            res.append(num)
        
        return res
        
def main():
    sol = Solution()
    print(sol.replaceNonCoprimes([6,4,3,2,7,6,2]))
    print(sol.replaceNonCoprimes([2,2,1,1,3,3,3]))

if __name__ == '__main__':
    main()