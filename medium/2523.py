from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[0] = False
        sieve[1] = False
        
        res = [-1, -1]
        min_diff = float('inf')

        for i in range(2, right + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False
        
        primes = [i for i in range(left, right + 1) if sieve[i]]
        
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                res = [primes[i], primes[i + 1]]
        
        return res
        
def main():
    sol = Solution()
    print(sol.closestPrimes(left = 10, right = 19))
    print(sol.closestPrimes(left = 4, right = 6))

if __name__ == '__main__':
    main()