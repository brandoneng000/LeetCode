from typing import List
from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                first_digit = int(str(nums[i])[0])
                last_digit = int(str(nums[j])[-1])
                
                if gcd(first_digit, last_digit) == 1:
                    res += 1
        
        return res

def main():
    sol = Solution()
    print(sol.countBeautifulPairs([2,5,1,4]))
    print(sol.countBeautifulPairs([11,21,12]))

if __name__ == '__main__':
    main()