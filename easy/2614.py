from typing import List
from math import sqrt

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def check_prime(num: int):
            if num <= 1:
                return False

            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False

            return True

        n = len(nums)
        res = 0

        for i in range(n):
            if check_prime(nums[i][i]):
                res = max(res, nums[i][i])
            
            if check_prime(nums[i][n - i - 1]):
                res = max(res, nums[i][n - i - 1])
        
        return res



        
def main():
    sol = Solution()
    print(sol.diagonalPrime([[1,2,3],[5,6,7],[9,10,11]]))
    print(sol.diagonalPrime([[1,2,3],[5,17,7],[9,11,10]]))

if __name__ == '__main__':
    main()