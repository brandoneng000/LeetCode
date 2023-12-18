from typing import List
from collections import Counter

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        products = Counter()
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                res += products[prod]
                products[prod] += 1
        
        return 8 * res
        
        
def main():
    sol = Solution()
    print(sol.tupleSameProduct([2,3,4,6,1,12]))
    print(sol.tupleSameProduct([2,3,4,6]))
    print(sol.tupleSameProduct([1,2,4,5,10]))

if __name__ == '__main__':
    main()