from typing import List

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primes(num: int):
            while num % 2 == 0:
                res.add(2)
                num //= 2
            
            for i in range(3, num + 1):
                while num % i == 0:
                    num //= i
                    res.add(i)
        
        res = set()

        for num in nums:
            primes(num)
        
        return len(res)

        
def main():
    sol = Solution()
    print(sol.distinctPrimeFactors([2,4,3,7,10,6]))
    print(sol.distinctPrimeFactors([2,4,8,16]))

if __name__ == '__main__':
    main()