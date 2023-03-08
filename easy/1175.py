import math

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(num: int) -> bool:
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0 and num != 2:
                    return False
            
            return num != 1
        
        primes = sum(is_prime(num) for num in range(1, n + 1))
        
        return math.factorial(primes) * math.factorial(n - primes) % (10**9 + 7)
    
def main():
    sol = Solution()
    print(sol.numPrimeArrangements(5))
    print(sol.numPrimeArrangements(100))
    print(sol.numPrimeArrangements(2))

if __name__ == '__main__':
    main()