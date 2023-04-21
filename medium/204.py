class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        sieve = [1] * n
        sieve[0] = 0
        sieve[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n, i):
                    sieve[j] = 0
        
        return sum(sieve)


def main():
    sol = Solution()
    print(sol.countPrimes(10))
    print(sol.countPrimes(0))
    print(sol.countPrimes(1))
    print(sol.countPrimes(5 * (10 ** 6)))

if __name__ == '__main__':
    main()