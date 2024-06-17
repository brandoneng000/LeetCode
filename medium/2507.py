from typing import List

class Solution:
    def smallestValue(self, n: int) -> int:
        def sieve_of_eratosthene():
            primes = [True] * (n + 1)
            primes[0] = False
            primes[1] = False

            for i in range(2, n + 1):
                if not primes[i]:
                    continue

                for j in range(i + i, n + 1, i):
                    primes[j] = False
            
            return [i for i in range(n + 1) if primes[i]]
        
        primes = sieve_of_eratosthene()
        
        while n not in primes:
            temp = n
            next = 0

            for p in primes:
                while temp % p == 0:
                    next += p
                    temp //= p
                
                if temp == 1:
                    break
            
            if n == next:
                return n
            
            n = next
        
        return n


def main():
    sol = Solution()
    print(sol.smallestValue(4))
    print(sol.smallestValue(15))
    print(sol.smallestValue(3))

if __name__ == '__main__':
    main()