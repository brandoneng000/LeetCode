from typing import List
from math import isqrt

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def seive(n: int):
            primes = [True for _ in range(n + 1)]
            primes[0] = False
            primes[1] = False
            i = 2

            while i * i <= n:
                if primes[i]:
                    for j in range(i * i, n + 1, i):
                        primes[j] = False
                i += 1
            
            return [i for i in range(n + 1) if primes[i]]

        # def seive(n: int):
        #     primes = []
        #     used = set()

        #     for i in range(2, n):
        #         if i in used:
        #             continue

        #         primes.append(i)

        #         for j in range(i * i, n, i):
        #             used.add(j)
            
        #     return primes

        primes = seive(n)
        primes_set = set(primes)
        res = []

        for prime in primes:
            if n - prime < prime:
                break

            if n - prime in primes_set:
                res.append([prime, n - prime])

        return res

def main():
    sol = Solution()
    print(sol.findPrimePairs(50))
    print(sol.findPrimePairs(10))
    print(sol.findPrimePairs(2))

if __name__ == '__main__':
    main()        